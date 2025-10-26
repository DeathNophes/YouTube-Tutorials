import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse", "Headphones", "Camera", "Printer", "Speaker"],
    "Units_Sold": [120, 200, 60, 90, 300, 250, 180, 70, 45, 110],
    "Unit_Price": [900, 500, 300, 200, 50, 45, 80, 350, 400, 150],
    "Region": ["North", "South", "North", "South", "North", "South", "North", "South", "North", "South"]
}

df = pd.DataFrame(data)
print("🔹 Original Data:")
print(df)

# -----------------------------
# Basic statistical functions
# -----------------------------

print("\n🔹 Average product price:")
print(df["Unit_Price"].mean())

print("\n🔹 Total units sold:")
print(df["Units_Sold"].sum())

print("\n🔹 Number of records (rows):")
print(df["Product"].count())

print("\n🔹 Minimum and maximum prices:")
print(f"Min: {df['Unit_Price'].min()} | Max: {df['Unit_Price'].max()}")

# -----------------------------
# Aggregation with filters and .loc[]
# -----------------------------

# Filter by region
north_sales = df.loc[df["Region"] == "North", "Units_Sold"].sum()
south_sales = df.loc[df["Region"] == "South", "Units_Sold"].sum()

print("\n🔹 Total units sold by region:")
print(f"North: {north_sales}, South: {south_sales}")

# Average product price in the North region
north_avg_price = df.loc[df["Region"] == "North", "Unit_Price"].mean()
print(f"\n🔹 Average price (North): {north_avg_price}")

# Min and max prices in the South region
south_min_price = df.loc[df["Region"] == "South", "Unit_Price"].min()
south_max_price = df.loc[df["Region"] == "South", "Unit_Price"].max()
print(f"\n🔹 Min and Max price (South): {south_min_price} / {south_max_price}")
