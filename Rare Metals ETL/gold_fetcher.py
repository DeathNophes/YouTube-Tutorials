import boto3
import json
import urllib.request
from botocore.exceptions import ClientError
from datetime import datetime
import csv
import io

BUCKET_NAME = "" # The name of your bucket
FILE_NAME = "" # The name of the file (Example: gold_prices.csv)

# --- Secrets Manager ---
def get_secret():
    secret_name = "" # The name of your secret in the Secrets Manager
    region_name = "" # The name of the region

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    secret_dict = json.loads(response['SecretString'])
    return secret_dict['x-access-token']

# --- Gold price API ---
def get_gold_price(api_key):
    url = "https://www.goldapi.io/api/XAU/USD"
    req = urllib.request.Request(url, headers={"x-access-token": api_key})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    return data

# --- S3 Handler ---
def append_to_s3(bucket_name, file_name, data_dict):
    s3 = boto3.client('s3')
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer, lineterminator='\n')

    try:
        obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        existing_csv = obj['Body'].read().decode('utf-8').splitlines()
        # Preserve existing rows
        for line in existing_csv:
            writer.writerow(line.split(','))
    except s3.exceptions.NoSuchKey:
        # File doesn’t exist yet, write header
        writer.writerow(["date", "gold_price_usd"])

    # Append the new row
    writer.writerow([data_dict["date"], data_dict["gold_price_usd"]])

    # Upload back to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())

# --- Lambda handler ---
def lambda_handler(event, context):
    api_key = get_secret()
    gold_data = get_gold_price(api_key)

    today = datetime.now().strftime("%Y-%m-%d")
    gold_price = gold_data.get("price")

    data_to_save = {
        "date": today,
        "gold_price_usd": gold_price
    }

    append_to_s3(BUCKET_NAME, FILE_NAME, data_to_save)
