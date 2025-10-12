import pandas as pd

# Sample DataFrame with 10 rows
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve",
             "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": [24, 30, 22, 28, 26, 35, 29, 23, 31, 27],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "New York",
             "Chicago", "Los Angeles", "Houston", "New York", "Chicago"],
    "Sales": [250, 400, 150, 300, 200, 500, 350, 180, 420, 310]
}
df = pd.DataFrame(data)
print(df)

# --- 1. Filtering with a single condition
print("People older than 25:")
print(df[df["Age"] > 25])

# --- 2. Filtering with multiple conditions using & (AND)
print("\nPeople older than 25 AND from New York:")
print(df[(df["Age"] > 25) & (df["City"] == "New York")])

# --- 3. Filtering with multiple conditions using | (OR)
print("\nPeople younger than 25 OR from Houston:")
print(df[(df["Age"] < 25) | (df["City"] == "Houston")])

# --- 4. Sorting by a column
print("\nData sorted by Age (ascending):")
print(df.sort_values(by="Age"))

print("\nData sorted by Age (descending):")
print(df.sort_values(by="Age", ascending=False))

# --- 5. Sorting by multiple columns
print("\nData sorted by City, then by Age:")
print(df.sort_values(by=["City", "Age"]))

# --- 6. Sorting by index
print("\nData sorted by index (ascending):")
print(df.sort_index())

print("\nData sorted by index (descending):")
print(df.sort_index(ascending=False))

# --- 7. Practical example: filter and sort
print("\nPeople from New York, sorted by Sales descending:")
ny_sorted = df[df["City"] == "New York"].sort_values(by="Sales", ascending=False)
print(ny_sorted)
