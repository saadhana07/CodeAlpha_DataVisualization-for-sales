import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

# Show data
print(df)

# Total Sales & Profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# Top Product (Sales)
top_product = df.loc[df['Sales'].idxmax()]
print("Top Product:", top_product['Product'])

# Top Region (Profit)
top_region = df.groupby('Region')['Profit'].sum().idxmax()
print("Top Region:", top_region)

# 📊 Chart 1: Sales by Product
plt.figure()
plt.bar(df['Product'], df['Sales'])
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.show()

# 📊 Chart 2: Profit by Product
profit_product = df.groupby('Product')['Profit'].sum()

plt.figure()
profit_product.plot(kind='bar')
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=30)
plt.show()

# 📊 Chart 3: Sales vs Profit Comparison
plt.figure()
plt.bar(df['Product'], df['Sales'], label='Sales')
plt.bar(df['Product'], df['Profit'], label='Profit')
plt.title("Sales vs Profit")
plt.xlabel("Product")
plt.ylabel("Amount")
plt.legend()
plt.xticks(rotation=30)
plt.show()

# 📊 Chart 4: Region-wise Profit (Pie)
profit_region = df.groupby('Region')['Profit'].sum()

plt.figure()
plt.pie(profit_region, labels=profit_region.index, autopct='%1.1f%%')
plt.title("Profit by Region")
plt.show()

# 🧠 Insights (Auto Print)
print("\n--- Insights ---")
print(f"Top selling product is {top_product['Product']}")
print(f"Most profitable region is {top_region}")
print("Higher sales products generally generate higher profit.")