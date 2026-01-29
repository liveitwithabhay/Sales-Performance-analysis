import pandas as pd

df = pd.read_csv("../data/cleaned_sales_data.csv")
df['year'] = pd.to_datetime(df['order_date']).dt.year

# YoY Growth
yoy = df.groupby('year')['revenue'].sum().pct_change() * 100
print("YoY Growth (%)")
print(yoy)

# CLV
clv = df.groupby('customer_id').agg({
    'order_id': 'count',
    'revenue': 'sum'
})
clv['avg_order_value'] = clv['revenue'] / clv['order_id']
print(clv.head())
