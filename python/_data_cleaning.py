import pandas as pd

df = pd.read_csv("../data/raw_sales_data.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

df.dropna(inplace=True)
df['profit'] = df['revenue'] - df['cost']

df.to_csv("../data/cleaned_sales_data.csv", index=False)
