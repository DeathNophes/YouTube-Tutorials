import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Julia"],
    "Age": [24, 30, None, 45, 28, 33, None, 29, 41, 36],
    "City": ["New York", "Los Angeles", "Chicago", None, "Miami", "Dallas", "Seattle", None, "Boston", "Denver"],
    "Salary": [50000, None, 62000, 58000, 52000, 61000, None, 49000, 65000, None]
}

df = pd.DataFrame(data)
print("🔹 Original DataFrame:")
print(df)

# -----------------------------
# Detecting missing values
# -----------------------------

print("\n🔹 Check where values are missing (True = missing):")
print(df.isna())

print("\n🔹 Count missing values per column:")
print(df.isna().sum())

print("\n🔹 Check where values are NOT missing:")
print(df.notna())

# -----------------------------
# Dropping missing data
# -----------------------------

# Drop rows that contain ANY NaN values
df_drop_rows = df.dropna()
print("\n🔹 DataFrame after dropping rows with missing values:")
print(df_drop_rows)

# Drop columns that contain ANY NaN values
df_drop_cols = df.dropna(axis=1)
print("\n🔹 DataFrame after dropping columns with missing values:")
print(df_drop_cols)

# -----------------------------
# Filling missing values
# -----------------------------

# Fill missing numerical values with the column mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing text values with a placeholder
df["City"] = df["City"].fillna("Unknown")

print("\n🔹 DataFrame after filling missing values:")
print(df)

# -----------------------------
# Example Workflow
# -----------------------------
# Example cleaning process:
# 1. Detect missing values
# 2. Fill numeric columns with averages
# 3. Replace missing cities with "Unknown"
# 4. Drop any remaining rows that still contain NaN (just to be safe)

clean_df = (
    df.fillna({
        "Age": df["Age"].mean(),
        "Salary": df["Salary"].mean(),
        "City": "Unknown"
    })
    .dropna()
)

print("\n🔹 Final cleaned DataFrame ready for analysis:")
print(clean_df)
