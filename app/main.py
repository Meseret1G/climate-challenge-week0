import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, filter_data

# Page configuration
st.set_page_config(page_title="Climate Data Dashboard", layout="wide")

st.title("🌍 Regional Climate Data Dashboard")
st.markdown("""
This dashboard visualizes climate insights for selected African countries. 
Explore trends in temperature, precipitation, and more.
""")

# Load data
@st.cache_data
def get_data():
    return load_data()

df = get_data()

if df.empty:
    st.error("No data found in the 'data' directory. Please ensure cleaned CSV files are present.")
else:
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Country multi-select
    all_countries = sorted(df['Country'].unique())
    selected_countries = st.sidebar.multiselect(
        "Select Countries", 
        options=all_countries, 
        default=all_countries
    )
    
    # Year range slider
    min_year = int(df['YEAR'].min())
    max_year = int(df['YEAR'].max())
    selected_years = st.sidebar.slider(
        "Select Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    
    # Variable selector
    variables = {
        "T2M": "Average Temperature (°C)",
        "PRECTOTCORR": "Precipitation (mm/day)",
        "RH2M": "Relative Humidity (%)",
        "WS2M": "Wind Speed (m/s)"
    }
    selected_var = st.sidebar.selectbox(
        "Select Variable",
        options=list(variables.keys()),
        format_func=lambda x: variables[x]
    )

    # Filter data
    filtered_df = filter_data(df, selected_countries, selected_years)

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    else:
        # Layout: Two columns for key metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"📈 {variables[selected_var]} Trend")
            # Group by Date and Country for the trend line
            trend_data = filtered_df.groupby(['Date', 'Country'])[selected_var].mean().reset_index()
            fig_line = px.line(
                trend_data, 
                x='Date', 
                y=selected_var, 
                color='Country',
                labels={selected_var: variables[selected_var]}
            )
            st.plotly_chart(fig_line, use_container_width=True)

        with col2:
            st.subheader(f"📊 {variables[selected_var]} Distribution")
            fig_box = px.box(
                filtered_df, 
                x='Country', 
                y=selected_var, 
                color='Country',
                labels={selected_var: variables[selected_var]}
            )
            st.plotly_chart(fig_box, use_container_width=True)

        # Additional Insight: Seasonal Heatmap or Correlation could go here
        st.subheader("📋 Raw Data Preview")
        st.dataframe(filtered_df.head(100), use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit & Plotly")
