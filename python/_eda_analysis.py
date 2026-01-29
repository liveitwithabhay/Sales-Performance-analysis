import pandas as pd

df = pd.read_csv("../data/cleaned_sales_data.csv")

print(df.describe())
print(df.groupby('region')['revenue'].sum())
print(df.groupby('product_category')['profit'].mean())
