# InsightCluster 👥 | Customer Persona Analysis

**InsightCluster** is an end-to-end Machine Learning pipeline that transforms raw retail transactions into actionable business segments. By utilizing **K-Means Clustering**, the system identifies distinct buyer personas based on demographics (Age, Gender) and financial behavior (Monetary value, Recency).

## 🚀 Live Interactive Dashboard
Experience the persona analysis here: [https://insight-cluster-retail.streamlit.app/](https://insight-cluster-retail.streamlit.app/)

## 🧠 The "Data Auditor" Approach
This project evolved from a standard RFM analysis to a **Demographic Profiling** system. 
- **The Challenge:** Initial data audit revealed a constant Frequency (1.0), making traditional RFM redundant.
- **The Solution:** Pivoted to a multi-dimensional feature set including Age and Gender, using **Log Transformation** and **Standard Scaling** to ensure balanced clusters.
- **The Result:** 4 distinct personas (VIPs, Premium Youth, At-Risk Seniors, and Standard Buyers) with tailored marketing strategies.

## 🛠️ Technical Stack
- **Engine:** Python 3.12+
- **Machine Learning:** Scikit-Learn (K-Means Clustering)
- **Data Engineering:** Pandas, NumPy
- **Visuals:** Plotly (Radar Charts, Horizontal Bar Analysis)
- **Deployment:** Streamlit Cloud

## 📁 Project Architecture
- `src/ingestion.py`: Data cleaning and standardizing.
- `src/processing.py`: Feature engineering and profile creation.
- `src/clustering.py`: K-Means training and model persistence.
- `src/dashboard.py`: Streamlit UI and business strategy mapping.

---
*Developed by Ulises Chustek.*
