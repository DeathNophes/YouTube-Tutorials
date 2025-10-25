import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard",
                "Mouse", "Headphones", "Camera", "Printer", "Speaker"],
    "Price": [1200, 800, 400, 300, 100, 50, 150, 600, 200, 250],
    "Quantity": [5, 10, 8, 6, 15, 20, 7, 4, 9, 12],
    "Discount": [0.10, 0.05, 0.08, 0.15, 0.00, 0.00, 0.05, 0.12, 0.10, 0.07]
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

# --- 1. Add a new column
df["Category"] = ["Electronics", "Electronics", "Electronics", "Electronics",
                  "Accessories", "Accessories", "Accessories", "Electronics",
                   "Electronics", "Accessories"]
print("\nAfter adding new column 'Category':")
print(df)

# --- 2. Recalculate an existing column or create a derived one
df["Total_Price"] = df["Price"] * df["Quantity"]
df["Discounted_Price"] = df["Total_Price"] * (1 - df["Discount"])
print("\nAfter calculating 'Total_Price' and 'Discounted_Price':")
print(df)

# --- 3. Drop a column
df_dropped_col = df.drop(columns=["Discount"])
print("\nAfter dropping the 'Discount' column:")
print(df_dropped_col)

# --- 4. Drop a row (for example, remove the first row)
df_dropped_row = df.drop(index=0)
print("\nAfter dropping the first row:")
print(df_dropped_row)

# --- 5. Rename columns
df_renamed = df.rename(columns={"Price": "Unit_Price", "Quantity": "Units_Sold"})
print("\nAfter renaming columns:")
print(df_renamed)

# --- 6. Practical example: new metric - Revenue per Unit
df["Revenue_per_Unit"] = df["Discounted_Price"] / df["Quantity"]
print("\nAdded new metric 'Revenue_per_Unit':")
print(df[["Product", "Discounted_Price", "Revenue_per_Unit"]])
