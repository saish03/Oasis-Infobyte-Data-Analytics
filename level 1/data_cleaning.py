import pandas as pd

df = pd.read_csv("retail_sales.csv")

# Check missing values
print(df.isnull().sum())

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower()

print("Cleaned Data")
print(df.head())