import pandas as pd
import datetime as dt

def generate_customer_features(input_path):
    print("--- Engineering Customer Profiles ---")
    df = pd.read_csv(input_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Snapshot for Recency
    snapshot_date = df['Date'].max() + dt.timedelta(days=1)
    
    # 1. Calculate Recency and Monetary per Customer
    # Since each customer is unique, we can keep Age and Gender
    profiles = df.groupby('Customer_ID').agg({
        'Date': lambda x: (snapshot_date - x.max()).days,
        'Total_Amount': 'sum',
        'Age': 'first',
        'Gender': 'first'
    })
    
    # 2. Convert Gender to Numeric (Binary Encoding)
    profiles['Gender'] = profiles['Gender'].map({'Male': 0, 'Female': 1})
    
    # Rename columns
    profiles.rename(columns={
        'Date': 'Recency',
        'Total_Amount': 'Monetary'
    }, inplace=True)
    
    profiles.to_csv('data/customer_profiles.csv')
    print(f"✅ Profiles created for {len(profiles)} unique customers.")

if __name__ == "__main__":
    generate_customer_features('data/cleaned_retail.csv')