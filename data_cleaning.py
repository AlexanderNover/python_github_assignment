# Purpose: Load a messy sales CSV, clean it, and save a cleaned version.
# This script standardizes column names, trims whitespace, handles missing values,
# and removes invalid rows such as negative quantities or negative prices.

import pandas as pd

# -------------------------------
# Load the raw dataset
# -------------------------------
def load_data(file_path: str):
    # Load raw CSV into DataFrame
    # Reason: We need to read the messy data into pandas before cleaning it
    return pd.read_csv(file_path)

# -------------------------------
# Clean and normalize column names
# -------------------------------
def clean_column_names(df):
    # Standardize column names for consistency across the dataset
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

# -------------------------------
# Trim whitespace in text columns
# -------------------------------
def trim_whitespace(df):
    # Remove extra spaces in string fields like product_name or category
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()
    return df

# -------------------------------
# Handle missing values
# -------------------------------
def handle_missing(df):
    # Drop any rows where price or quantity is missing
    df = df.dropna(subset=["price", "quantity"])
    return df

# -------------------------------
# Remove invalid rows
# -------------------------------
def remove_invalid(df):
    # Remove rows that have negative or impossible values
    df = df[df["price"] >= 0]
    df = df[df["quantity"] >= 0]
    return df

# -------------------------------
# Run full cleaning pipeline
# -------------------------------
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df = load_data(raw_path)
    df = clean_column_names(df)
    df = trim_whitespace(df)
    df = handle_missing(df)
    df = remove_invalid(df)

    df.to_csv(cleaned_path, index=False)
    print("Cleaning complete. Preview:")
    print(df.head())