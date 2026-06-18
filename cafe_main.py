import pandas as pd
import numpy as np

df = pd.read_csv('dirty_cafe_sales.csv')

df.columns = df.columns.str.strip()
print(f"Data is loaded: {df.shape}")

str_cols = df.select_dtypes(include=['object']).columns
for col in str_cols:
    df[col] = df[col].astype(str).str.strip()
print("Whitespaces is stripped from columns")

invalid = ['ERROR', 'UNKNOWN', 'unknown', 'error', 'nan', 'NaN', 'NAN', '']
df = df.replace(invalid, np.nan)
print("Invalid markers replace with NaN")

df = df.drop_duplicates()
df = df.drop_duplicates(subset=['Transaction ID'])
print(f"After removing duplicates: {df.shape}")

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
mask_price = df['Price Per Unit'].isna() & df['Total Spent'].notna() & df['Quantity'].notna()
df.loc[mask_price, 'Price Per Unit'] = df.loc[mask_price, 'Total Spent'] / df.loc[mask_price, 'Quantity']
mask_total = df['Total Spent'].isna() & df['Price Per Unit'].notna() & df['Quantity'].notna()
df.loc[mask_total, 'Total Spent'] = df.loc[mask_total, 'Quantity'] * df.loc[mask_total, 'Price Per Unit']
df['Price Per Unit'] = df['Price Per Unit'].round(2)
df['Total Spent'] = df['Total Spent'].round(2)
print("Numeric columns fixed")

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
df = df.dropna(subset=['Transaction Date'])
df['Transaction Date'] = df['Transaction Date'].dt.strftime('%y-%m-%d')
print("Date column fixed (single column, YYYY-MMMM-DDDD)")

if df['Item'].mode().notna().any():
    item_mode = df['Item'].mode()[0]
    df['Item'] = df['Item'].fillna(item_mode)
if df['Payment Method'].mode().notna().any():
    pay_mode = df['Payment Method'].mode()[0]
    df['Payment Method'] = df['Payment Method'].fillna(pay_mode)
    
df['Location'] = df['Location'].replace('True', np.nan)
if df['Location'].mode().notna().any():
    loc_mode = df['Location'].mode()[0]
    df['Location'] = df['Location'].fillna(loc_mode)
print("Missing categorical values filled with mode")

df = df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent'])
print(f"After dropping rows with missing numeric values: {df.shape}")
df.to_csv('cafe_sales1.csv', index=False)
print("file is saved")
print(f"final shape: {df.shape}")
