import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 28],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
df.to_csv("example.csv", index=True)
print(df)

# --- .loc[] examples (label-based indexing)
print(df.loc[0])
print(df.loc[0, "Name"])
print(df.loc[:, "Age"])
print(df.loc[1:3, ["Name", "City"]])

# --- .iloc[] examples (position-based indexing)
print(df.iloc[0])
print(df.iloc[0, 1])
print(df.iloc[:, 2])
print(df.iloc[1:3, 0:2])

# --- Compare .loc[] vs .iloc[]
print(df.loc[0:2])
print("-----------------------")
print(df.iloc[0:2])

# --- Boolean filtering
print(df["Age"] > 25)
print(df[df["Age"] > 25])
print(df[df["City"] == "Chicago"])
print(df[(df["Age"] > 23) & (df["City"] == "New York")])
print(df[(df["Age"] < 30) | (df["City"] == "Houston")])

# --- Combine boolean mask with .loc[]
print(df.loc[df["Age"] > 25, ["Name", "City"]])

# --- Comparison summary (.loc[] vs .iloc[])
print(df.loc[0:2, "Name":"City"])
print("-----------------------")
print(df.iloc[0:2, 0:3])
