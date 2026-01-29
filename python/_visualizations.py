import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_sales_data.csv")

# Revenue by Region
plt.figure()
df.groupby('region')['revenue'].sum().plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# Profit Leakage
plt.figure()
df[df['profit'] < 0].groupby('product_name')['profit'].sum().plot(kind='bar')
plt.title("Loss-Making Products")
plt.xlabel("Product")
plt.ylabel("Loss")
plt.show()
