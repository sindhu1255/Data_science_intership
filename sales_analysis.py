import pandas as pd

# Load Dataset
df = pd.read_csv('sales_data.csv')

# Display Dataset
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicate Records
df = df.drop_duplicates()

# Handle Missing Values
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('Unknown')

# Sales Analysis
total_revenue = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
highest_sale = df['Total_Sales'].max()
lowest_sale = df['Total_Sales'].min()

print("\nSales Analysis:")
print("Total Revenue:", total_revenue)
print("Average Sales:", average_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)

# Best Selling Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

print("Best Selling Product:", best_product)

print("\nAnalysis Completed Successfully!")
