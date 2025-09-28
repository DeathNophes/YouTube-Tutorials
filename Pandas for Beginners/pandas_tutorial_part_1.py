import pandas as pd

# Create Series (one column of data)
prices = pd.Series([120, 15, 85])
print(prices)

# Create DataFrame (table)
data = {
    "Product": ["Gold", "Silver", "Oil"],
    "Price": [120, 15, 85],
    "Currency": ["USD", "USD", "USD"]
}
df = pd.DataFrame(data)
print(df)
