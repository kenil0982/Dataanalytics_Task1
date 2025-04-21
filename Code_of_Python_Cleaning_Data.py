# Step 1: Import libraries
import pandas as pd
import numpy as np

# Step 2: Load dataset (update file path as needed on Kaggle)
df = pd.read_csv("/kaggle/input/blinkit-grocery-data/BlinkIT_Grocery_Data.csv")  # or .xlsx with openpyxl

# Step 3: View basic structure
print(df.info())
print(df.head())

# Step 4: Handle Missing Values (Item Weight)
df["Item Weight"].fillna(df["Item Weight"].mean(), inplace=True)

# Step 5: Remove Duplicates
df.drop_duplicates(inplace=True)

# Step 6: Standardize 'Item Fat Content'
df["Item Fat Content"] = df["Item Fat Content"].replace({
    "LF": "Low Fat",
    "low fat": "Low Fat",
    "reg": "Regular"
})

# Step 7: Convert 'Outlet Establishment Year' to datetime
df["Outlet Establishment Year"] = pd.to_datetime(df["Outlet Establishment Year"], format='%Y', errors='coerce')

# Step 8: Rename Columns (lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 9: Fix Data Types
df["rating"] = df["rating"].astype(int)
df["sales"] = df["sales"].astype(float)

# Optional: Save cleaned file (for output in Kaggle notebook)
df.to_csv("/kaggle/working/BlinkIT_Grocery_Cleaned.csv", index=False)

# View cleaned data
df.head()
