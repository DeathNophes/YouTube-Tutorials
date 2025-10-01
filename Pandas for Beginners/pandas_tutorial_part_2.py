import pandas as pd

df_csv = pd.read_csv("data/part_2/sample_data.csv")
print(df_csv)

df_json = pd.read_json("data/part_2/sample_data.json")
print(df_json)

print(df_json.head())
print(df_json.tail())
print(df_json.info())
print(df_json.describe(include="all"))

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

df.to_csv("people.csv", index=False)

df.to_json("people.json", orient="records", indent=4)
