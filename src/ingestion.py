import pandas as pd
import os

def load_and_clean_data(input_path):
    print(f"--- Loading dataset from {input_path} ---")
    if not os.path.exists(input_path):
        print(f"❌ Error: {input_path} not found. Check the file name and path.")
        return
    
    # Reading the specific retail dataset
    df = pd.read_csv(input_path)
    
    # Standardizing column names for easier coding
    df.columns = [col.replace(' ', '_') for col in df.columns]
    
    # Convert Date to datetime format for RFM calculation
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Clean data: drop rows missing crucial identification or financial data
    df = df.dropna(subset=['Customer_ID', 'Total_Amount'])
    
    print(f"✅ Data loaded successfully: {len(df)} records found.")
    
    # Save the intermediate cleaned file
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/cleaned_retail.csv', index=False)

if __name__ == "__main__":
    # Pointing to your specific CSV name
    load_and_clean_data('data/retail_sales_dataset.csv')