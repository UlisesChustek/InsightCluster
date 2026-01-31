import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def run_clustering(input_path, n_clusters=4):
    print(f"--- Running Profiling Cluster (K={n_clusters}) ---")
    df = pd.read_csv(input_path, index_col='Customer_ID')
    
    # Handle skewness in Monetary and Recency with Log Transform
    # We don't log Age or Gender as they are bounded
    df_transformed = df.copy()
    df_transformed['Monetary'] = np.log1p(df_transformed['Monetary'])
    df_transformed['Recency'] = np.log1p(df_transformed['Recency'])
    
    # Scaling is mandatory
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_transformed)
    
    # KMeans
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['Cluster'] = model.fit_predict(scaled_data)
    
    # Save
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/cluster_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    df.to_csv('data/clustered_customers.csv')
    
    print("✅ Clustering complete based on Age, Gender, Spend, and Recency.")

if __name__ == "__main__":
    run_clustering('data/customer_profiles.csv')