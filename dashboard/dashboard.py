import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

st.set_page_config(page_title="Sales Optimization Dashboard", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stMetric { border: 1px solid #e6e9ef; padding: 10px; border-radius: 5px; background: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA SIMULATION ENGINE ---
# In production, replace this with: 
# df = pd.read_sql("SELECT * FROM sales_table", connection) 
def get_optimized_data():
    regions = ['North America', 'EMEA', 'APAC', 'LATAM']
    categories = ['SaaS Subscriptions', 'Professional Services', 'Hardware']
    data = []
    for _ in range(200):
        revenue = np.random.uniform(1000, 5000)
        cost = revenue * np.random.uniform(0.4, 0.8) # Simulating margin
        data.append({
            'Date': pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(0, 365), unit='d'),
            'Region': np.random.choice(regions),
            'Category': np.random.choice(categories),
            'Revenue': revenue,
            'Cost': cost,
            'Margin': revenue - cost,
            'Customer_ID': np.random.randint(1000, 1100)
        })
    return pd.DataFrame(data)

st.title("🛡️ Revenue Optimization & Sales Analysis")
st.caption("Tracking Region-wise Revenue Leakage and Margin Inefficiencies")

placeholder = st.empty()

while True:
    df = get_optimized_data()
    
    # CALCULATE METRICS
    total_rev = df['Revenue'].sum()
    avg_margin = (df['Margin'].sum() / total_rev) * 100
    clv = df.groupby('Customer_ID')['Revenue'].sum().mean()

    with placeholder.container():
        # --- EXECUTIVE KPIS ---
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Total Revenue", f"${total_rev/1e6:.2f}M", "YoY +12.5%")
        kpi2.metric("Contribution Margin", f"{avg_margin:.1f}%", "-2.3%", delta_color="inverse")
        kpi3.metric("Avg CLV", f"${clv:,.0f}")
        kpi4.metric("Revenue Leakage Est.", "$42.5K", delta_color="off")

        st.divider()

        # --- REVENUE LEAKAGE & MARGIN ANALYSIS ---
        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("Region-wise Margin Inefficiency")
            # Identifying where margin is lower than target (60%)
            margin_analysis = df.groupby('Region')[['Revenue', 'Margin']].sum()
            margin_analysis['Margin %'] = (margin_analysis['Margin'] / margin_analysis['Revenue']) * 100
            fig_margin = px.bar(margin_analysis.reset_index(), x='Region', y='Margin %', 
                                 color='Margin %', color_continuous_scale='RdYlGn',
                                 range_color=[30, 70])
            st.plotly_chart(fig_margin, use_container_width=True)

        with col_right:
            st.subheader("Revenue Contribution by Category")
            fig_pie = px.pie(df, values='Revenue', names='Category', hole=0.4)
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- YOY GROWTH TREND ---
        st.subheader("YoY Sales Growth Trend")
        df_trend = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum().reset_index()
        df_trend['Date'] = df_trend['Date'].dt.to_timestamp()
        st.area_chart(df_trend.set_index('Date'))

    time.sleep(10) # Refresh every 10 seconds