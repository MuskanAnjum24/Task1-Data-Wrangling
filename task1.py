import pandas as pd

# Load dataset
data = pd.read_csv("SuperStoreOrders.csv")

# Show first 5 rows
print("FIRST 5 ROWS")
print(data.head())

# Dataset information
print("\nDATASET INFO")
print(data.info())

# Check missing values
print("\nMISSING VALUES")
print(data.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS")
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Convert mixed date formats
data['order_date'] = pd.to_datetime(
    data['order_date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

data['ship_date'] = pd.to_datetime(
    data['ship_date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

# Convert sales column to numeric
data['sales'] = pd.to_numeric(data['sales'], errors='coerce')

# Create total sales column
data['total_sales'] = data['sales'] * data['quantity']

# Display cleaned data
print("\nCLEANED DATA")
print(data.head())

# Save cleaned dataset
data.to_csv("Cleaned_Superstore.csv", index=False)

print("\nDATA CLEANING COMPLETED")
print("Cleaned dataset saved as Cleaned_Superstore.csv")