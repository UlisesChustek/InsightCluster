import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# UI Configuration
st.set_page_config(page_title="InsightCluster | Persona Analysis", layout="wide")
st.title("👥 InsightCluster: Customer Persona Dashboard")

# Load Data
@st.cache_resource
def load_data():
    return pd.read_csv('data/clustered_customers.csv')

df = load_data()

# 1. Calculate Cluster Personas (Averages)
cluster_stats = df.groupby('Cluster').agg({
    'Age': 'mean',
    'Gender': 'mean', # Proportion of Females
    'Monetary': 'mean',
    'Recency': 'mean'
}).reset_index()

# Map numeric clusters to "Business Names" for better UX
persona_map = {
    0: "Standard Buyers",
    1: "Premium Youth",
    2: "At-Risk Seniors",
    3: "VIP Customers"
}
cluster_stats['Persona'] = cluster_stats['Cluster'].map(persona_map)

# --- UI Layout ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Financial Performance by Segment")
    # Horizontal Bar Chart to solve the "vertical label" UX issue
    fig_money = px.bar(
        cluster_stats, 
        y='Persona', 
        x='Monetary', 
        color='Persona',
        orientation='h',
        title='Average Revenue per Transaction ($)',
        labels={'Monetary': 'Avg Spend', 'Persona': 'Customer Type'},
        template='plotly_dark'
    )
    st.plotly_chart(fig_money, use_container_width=True)

with col2:
    st.subheader("Demographic Split (Gender %)")
    # Showing Gender as a percentage of Females per cluster
    fig_gender = px.bar(
        cluster_stats,
        y='Persona',
        x='Gender',
        orientation='h',
        title='Proportion of Female Customers',
        labels={'Gender': '% Female'},
        color_discrete_sequence=['#ff66b2'],
        template='plotly_dark'
    )
    st.plotly_chart(fig_gender, use_container_width=True)

st.divider()

# 2. Radar Chart: The "DNA" of the Groups
st.subheader("Customer Segment DNA (Radar Analysis)")

# Normalize data for the Radar chart (0 to 1 scale) to make them comparable
categories = ['Age', 'Monetary', 'Recency']
fig_radar = go.Figure()

for i, row in cluster_stats.iterrows():
    fig_radar.add_trace(go.Scatterpolar(
        r=[row['Age']/60, row['Monetary']/1500, row['Recency']/365], # Rough normalization
        theta=categories,
        fill='toself',
        name=row['Persona']
    ))

fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    showlegend=True,
    template='plotly_dark'
)
st.plotly_chart(fig_radar, use_container_width=True)

# 3. Strategy Table
st.subheader("Marketing Strategy Recommendations")
st.table(cluster_stats[['Persona', 'Age', 'Monetary', 'Recency']])