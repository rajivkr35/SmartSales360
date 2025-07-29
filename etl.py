import pandas as pd

# Step 1: Load raw dataset
df_raw = pd.read_csv("indian_ecommerce_raw.csv")

# Step 2: Remove duplicates
df_cleaned = df_raw.drop_duplicates()

# Step 3: Handle missing values
df_cleaned['customer_city'] = df_cleaned['customer_city'].fillna("Unknown")
df_cleaned['payment_mode'] = df_cleaned['payment_mode'].fillna("Unknown")
df_cleaned['discount_percent'] = df_cleaned['discount_percent'].fillna(0)

# Step 4: Convert data types
df_cleaned['discount_percent'] = df_cleaned['discount_percent'].astype(float)
df_cleaned['quantity'] = df_cleaned['quantity'].astype(int)
df_cleaned['unit_price'] = df_cleaned['unit_price'].astype(float)
df_cleaned['cost_price'] = df_cleaned['cost_price'].astype(float)
df_cleaned['is_returned'] = df_cleaned['is_returned'].astype(int)
df_cleaned['delivery_time_days'] = df_cleaned['delivery_time_days'].astype(int)

# Step 5: Feature Engineering
df_cleaned['revenue'] = df_cleaned['unit_price'] * df_cleaned['quantity'] * (1 - df_cleaned['discount_percent'] / 100)
df_cleaned['cost'] = df_cleaned['cost_price'] * df_cleaned['quantity']
df_cleaned['net_profit'] = df_cleaned['revenue'] - df_cleaned['cost']
df_cleaned['return_loss'] = df_cleaned['revenue'] * df_cleaned['is_returned']

# Step 6: Save the cleaned dataset
df_cleaned.to_csv("indian_ecommerce_cleaned.csv", index=False)

print("✅ ETL complete. Cleaned dataset saved as 'indian_ecommerce_cleaned.csv'")
