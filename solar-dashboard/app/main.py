import streamlit as st
import pandas as pd
from utils import load_country_data, boxplot_ghi, top_regions_table

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("Solar Data Dashboard")

# 1. Select country
country = st.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])

# 2. Map country to actual CSV file
file_mapping = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierraleone_clean.csv",
    "Togo": "data/togo_clean.csv"
}

data_file = file_mapping[country]

# 3. Load data
df = None
try:
    df = load_country_data(data_file)
except FileNotFoundError:
    st.error(f"Data for {country} not found in 'data/' directory.")
    st.stop()

# 4. Only proceed if df is loaded
if df is not None and not df.empty:
    # Optional date filtering
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        min_date = df['Timestamp'].min()
        max_date = df['Timestamp'].max()
        if pd.notnull(min_date) and pd.notnull(max_date):
            selected_dates = st.slider(
                "Select Date Range",
                min_value=min_date.to_pydatetime(),
                max_value=max_date.to_pydatetime(),
                value=(min_date.to_pydatetime(), max_date.to_pydatetime())
            )
            df = df[(df['Timestamp'] >= selected_dates[0]) & (df['Timestamp'] <= selected_dates[1])]

    # 5. Boxplot of GHI
    st.subheader("GHI Boxplot")
    st.plotly_chart(boxplot_ghi(df, country), use_container_width=True)

    # 6. Top regions table
    st.subheader("Top Regions by GHI")
    st.dataframe(top_regions_table(df))
else:
    st.warning("No data available for this country.")

