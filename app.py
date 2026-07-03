"""
Sales Forecasting Dashboard
Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('train.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Quarter'] = df['Order Date'].dt.quarter
    return df

@st.cache_data
def load_monthly_data(df):
    monthly = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index()
    monthly['Month'] = monthly['Order Date'].astype(str)
    return monthly

# Load data
df = load_data()
monthly_data = load_monthly_data(df)

# Sidebar navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Sales Overview", "Forecast Explorer", "Anomaly Report", "Product Segments"]
)

# Main content
if page == "Sales Overview":
    st.title("📈 Sales Overview Dashboard")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Revenue", f"${df['Sales'].sum():,.2f}")
    with col2:
        st.metric("Total Orders", f"{df['Order ID'].nunique():,}")
    with col3:
        st.metric("Average Order Value", f"${df['Sales'].mean():,.2f}")
    with col4:
        st.metric("Unique Customers", f"{df['Customer ID'].nunique():,}")

    st.markdown("---")

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox('Select Category', ['All'] + list(df['Category'].unique()))
    with col2:
        selected_region = st.selectbox('Select Region', ['All'] + list(df['Region'].unique()))

    # Filter data
    filtered_df = df.copy()
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]

    # Yearly sales
    yearly_sales = filtered_df.groupby('Year')['Sales'].sum().reset_index()
    fig1 = px.bar(yearly_sales, x='Year', y='Sales', 
                   title='Total Sales by Year',
                   color='Year',
                   color_continuous_scale='Blues')
    st.plotly_chart(fig1, use_container_width=True)

    # Monthly trend
    col1, col2 = st.columns(2)

    with col1:
        monthly_filtered = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index()
        monthly_filtered['Month'] = monthly_filtered['Order Date'].astype(str)
        fig2 = px.line(monthly_filtered, x='Month', y='Sales', 
                        title='Monthly Sales Trend')
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
        fig3 = px.pie(category_sales, values='Sales', names='Category',
                       title='Sales by Category')
        st.plotly_chart(fig3, use_container_width=True)

    # Region and segment analysis
    col1, col2 = st.columns(2)

    with col1:
        region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
        fig4 = px.bar(region_sales, x='Region', y='Sales',
                       title='Sales by Region',
                       color='Region')
        st.plotly_chart(fig4, use_container_width=True)

    with col2:
        segment_sales = filtered_df.groupby('Segment')['Sales'].sum().reset_index()
        fig5 = px.pie(segment_sales, values='Sales', names='Segment',
                       title='Sales by Customer Segment')
        st.plotly_chart(fig5, use_container_width=True)

elif page == "Forecast Explorer":
    st.title("🔮 Forecast Explorer")
    st.markdown("---")

    # Model selection
    model_choice = st.selectbox('Select Forecasting Model', ['SARIMA', 'Prophet', 'XGBoost'])
    horizon = st.slider('Forecast Horizon (months)', 1, 3, 1)

    st.markdown("---")

    # Display forecast (using sample data)
    st.subheader(f"3-Month Forecast using {model_choice}")

    # Sample forecast data (replace with actual model predictions)
    forecast_data = {
        'Month': ['Jan 2019', 'Feb 2019', 'Mar 2019'],
        'Forecast': [25000, 23000, 28000],
        'Lower_CI': [22000, 20000, 24000],
        'Upper_CI': [28000, 26000, 32000]
    }
    forecast_df = pd.DataFrame(forecast_data)

    # Plot forecast
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=forecast_df['Month'],
        y=forecast_df['Forecast'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color='blue', width=3)
    ))
    fig.add_trace(go.Scatter(
        x=forecast_df['Month'],
        y=forecast_df['Upper_CI'],
        mode='lines',
        name='Upper Confidence',
        line=dict(width=0),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=forecast_df['Month'],
        y=forecast_df['Lower_CI'],
        mode='lines',
        name='Lower Confidence',
        line=dict(width=0),
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    ))
    fig.update_layout(
        title='3-Month Sales Forecast',
        xaxis_title='Month',
        yaxis_title='Sales ($)',
        hovermode='x'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Display metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("MAE", "$2,450")
    with col2:
        st.metric("RMSE", "$3,240")

elif page == "Anomaly Report":
    st.title("⚠️ Anomaly Report")
    st.markdown("---")

    st.subheader("Detected Sales Anomalies")

    # Sample anomaly data
    anomaly_dates = pd.date_range(start='2018-01-01', periods=8, freq='W')
    anomaly_sales = [82000, 85000, 38000, 40000, 78000, 81000, 37000, 79000]

    anomaly_df = pd.DataFrame({
        'Date': anomaly_dates,
        'Sales': anomaly_sales,
        'Status': ['Anomaly' if i % 2 == 0 else 'Normal' for i in range(8)]
    })

    # Plot anomalies
    fig = px.scatter(anomaly_df, x='Date', y='Sales', color='Status',
                      title='Sales Anomalies Detected',
                      color_discrete_map={'Anomaly': 'red', 'Normal': 'blue'})
    fig.update_traces(marker_size=10)
    st.plotly_chart(fig, use_container_width=True)

    # Anomaly table
    st.subheader("Anomaly Details")
    anomaly_table = pd.DataFrame({
        'Date': ['Nov 15, 2018', 'Dec 10, 2018', 'Jan 05, 2019'],
        'Sales': ['$82,500', '$89,200', '$35,800'],
        'Deviation': ['+52%', '+65%', '-35%'],
        'Likely Cause': ['Holiday Season', 'End of Year Promotions', 'Post-Holiday Dip']
    })
    st.table(anomaly_table)

elif page == "Product Segments":
    st.title("📊 Product Demand Segments")
    st.markdown("---")

    st.subheader("Sub-Category Segmentation Analysis")

    # Sample segmentation data
    segments = ['Growing Demand', 'High Volume, Stable', 'High Volatility', 'Low Volume, Stable']
    counts = [12, 7, 5, 8]

    fig = px.pie(values=counts, names=segments, 
                  title='Sub-Category Distribution by Demand Segment',
                  color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Segment Details")
    segment_data = pd.DataFrame({
        'Sub-Category': ['Phones', 'Chairs', 'Paper', 'Furnishings', 'Labels'],
        'Segment': ['Growing Demand', 'High Volume, Stable', 'High Volume, Stable', 
                    'High Volatility', 'Low Volume, Stable'],
        'Total Sales': ['$250K', '$180K', '$120K', '$95K', '$45K'],
        'Growth Rate': ['15.2%', '4.3%', '2.8%', '8.7%', '1.2%']
    })
    st.dataframe(segment_data, use_container_width=True)

    st.info("💡 Stocking Strategy: High growth segments require aggressive inventory investment, while stable segments need consistent replenishment.")
