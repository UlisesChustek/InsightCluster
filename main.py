from src.ingestion import load_and_clean_data
from src.processing import generate_rfm_metrics
from src.clustering import run_clustering

def start_pipeline():
    print("🚀 InsightCluster: Customer Segmentation Pipeline Started")
    
    # Updated with your correct filename
    load_and_clean_data('data/retail_sales_dataset.csv')
    
    # Process RFM metrics from the cleaned data
    generate_rfm_metrics('data/cleaned_retail.csv')
    
    # Run K-Means with 4 clusters
    run_clustering('data/rfm_data.csv', n_clusters=4)
    
    print("✅ InsightCluster pipeline execution finished successfully.")

if __name__ == "__main__":
    start_pipeline()