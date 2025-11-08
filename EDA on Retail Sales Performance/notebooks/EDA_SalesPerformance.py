import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import os
print(os.getcwd())

# load data

df = pd.read_csv(
    r"data/superstor_dataset.csv",
    encoding='latin1'
)
# Once you fix the typo and use encoding='latin1', it should load perfectly.

# Preview
df.head()

df.info()
df.describe()
df.shape
df.columns


# Drop duplicates
df.drop_duplicates(inplace=True)

# Check missing values
df.isnull().sum()

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

sns.histplot(df['Sales'], kde=True, color='skyblue')
plt.title('Sales Distribution', fontsize=15, fontweight='bold', color='navy')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()


sns.boxplot(x='Profit', data=df, color='orange')
plt.title('Profit Spread Across Orders', fontsize=15, fontweight='bold', color='darkred')
plt.xlabel('Profit Value')
plt.show()

sns.scatterplot(x='Sales', y='Profit', data=df, color='green', alpha=0.7)
plt.title('Sales vs Profit Relationship', fontsize=15, fontweight='bold')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()


sns.barplot(x='Category', y='Sales', data=df, palette='viridis')
plt.title('Sales by Product Category', fontsize=15, fontweight='bold', color='darkgreen')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()


df['Order Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Order Month')['Sales'].sum()

monthly_sales.plot(kind='line', figsize=(10,5), marker='o', color='blue')
plt.title('Monthly Sales Trend', fontsize=15, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()


region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=region_sales.index, y=region_sales.values, palette='cool')
plt.title('Sales Performance by Region', fontsize=15, fontweight='bold', color='darkblue')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=region_sales.index, y=region_sales.values, palette='cool')
plt.title('Sales Performance by Region', fontsize=15, fontweight='bold', color='darkblue')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()


sns.scatterplot(x='Discount', y='Profit', data=df, hue='Category', palette='Set2')
plt.title('Impact of Discount on Profit', fontsize=15, fontweight='bold', color='purple')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.legend(title='Category')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap (Numeric Variables)', fontsize=15, fontweight='bold')
plt.show()

pivot = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')
sns.heatmap(pivot, annot=True, cmap='YlGnBu')
plt.title('Sales by Category and Region', fontsize=15, fontweight='bold')
plt.show()

sns.barplot(x='Segment', y='Profit', data=df, palette='magma')
plt.title('Profit by Customer Segment', fontsize=15, fontweight='bold', color='darkred')
plt.xlabel('Customer Segment')
plt.ylabel('Total Profit')
plt.show()


df.to_csv('outputs/cleaned_data.csv', index=False)
plt.savefig('outputs/charts/sales_trend.png')























