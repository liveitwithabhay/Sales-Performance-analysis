import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Advanced Sales Analytics", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Enterprise Sales Performance Tracker")

placeholder = st.empty()

while True:
    # --- DATA SOURCE ---
    # In a real scenario, use: df = pd.read_csv('data/your_file.csv')
    # For now, we simulate "live" data with random variations
    df = pd.DataFrame({
        'Timestamp': pd.date_range(start='1/1/2026', periods=100, freq='H'),
        'Revenue': np.random.randint(100, 500, size=100),
        'Orders': np.random.randint(1, 10, size=100),
        'Category': np.random.choice(['Electronics', 'Apparel', 'Home', 'Beauty'], size=100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100)
    })

    with placeholder.container():
        # --- ROW 1: TOP KEY METRICS ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}", "+12%")
        col2.metric("Total Orders", f"{df['Orders'].sum()}", "+5%")
        col3.metric("Avg Order Value", f"${df['Revenue'].mean():.2f}", "-2%")
        col4.metric("Active Regions", df['Region'].nunique())

        st.divider()

        # --- ROW 2: TRENDS & CATEGORIES ---
        left_chart, right_chart = st.columns(2)
        
        with left_chart:
            st.subheader("📈 Revenue Over Time")
            st.line_chart(df.set_index('Timestamp')['Revenue'])

        with right_chart:
            st.subheader("📦 Sales by Category")
            category_data = df.groupby('Category')['Revenue'].sum()
            st.bar_chart(category_data)

        # --- ROW 3: DETAILED ANALYSIS ---
        st.subheader("📍 Regional Performance Distribution")
        regional_df = df.groupby('Region')[['Revenue', 'Orders']].sum()
        st.area_chart(regional_df)

        # --- ROW 4: DATA TABLE ---
        with st.expander("View Raw Transaction Log"):
            st.dataframe(df.sort_values('Timestamp', ascending=False), use_container_width=True)

    time.sleep(5)