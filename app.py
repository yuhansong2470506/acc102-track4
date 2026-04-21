import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------- Basic settings of the page ----------------------
st.set_page_config(
    page_title="Air Quality Tool | ACC102 Track4",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Introduction
st.title("🌬️ Air Quality Tool (ACC102 Track4)")
st.markdown("This is an interactive air quality data analysis tool supporting data preview, trend analysis, and pollutant comparison.")

# ----------------------  Load Data ----------------------
# Read the CSV file uploaded to the repository
df = pd.read_csv("air_quality.csv")
df["Date"] = pd.to_datetime(df["Date"])  # Convert date format

# ---------------------- Sidebar Filters  ----------------------
st.sidebar.header("Filter Settings")

# City screening
city_list = df["City"].unique()
selected_cities = st.sidebar.multiselect(
    "city",
    options=city_list,
    default=city_list[0]
)

# Date range screening
min_date = df["Date"].min()
max_date = df["Date"].max()
selected_dates = st.sidebar.date_input(
    "time range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Apply filter criteria
filtered_df = df[
(df["City"].isin(selected_cities)) &
(df["Date"] >= pd.to_datetime(selected_dates[0])) &
(df["Date"] <= pd.to_datetime(selected_dates[1]))
]

# ---------------------- Key Air Quality Metrics ----------------------
st.subheader('📈 Key Air Quality Metrics')

# Key indicator cards
col1, col2, col3 = st.columns(3)
col1.metric("AverageQI", round(filtered_df["AQI"].mean(), 1))
col2.metric("HighestAQI", filtered_df["AQI"].max())
col3.metric("LowestAQI", filtered_df["AQI"].min())

# Key Air Quality Metrics
st.dataframe(filtered_df, use_container_width=True)

# ---------------------- Visual Chart ----------------------
# 1. AQI Time trend chart
st.subheader('📈 AQI The trend of time change')
fig_aqi = px.line(
filtered_df,
x="Date",
y="AQI",
color="City",
title="The trend of AOI in different cities over time",
labels={"AQI": "Air Quality Index(AQI)", "Date": "date"}
)
st.plotly_chart(fig_aqi, use_container_width=True)

# 2. Comparison of pollutant concentration
st.subheader('📊 Comparison of the average concentration of major pollutants')
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "O3"]
avg_pollutants = filtered_df.groupby("City")[pollutants].mean().reset_index()
fig_pollutants = px.bar(
avg_pollutants,
x="City",
y=pollutants,
barmode="group",
title="The average concentration of major pollutants in different cities"
)
st.plotly_chart(fig_pollutants, use_container_width=True)

# 3. Air quality level distribution
st.subheader('📊Air quality level distribution ')
fig_level = px.pie(
filtered_df,
names="Quality_Level",
title="Disteibution of the proportion of air quality grade",
hole=0.3
)
st.plotly_chart(fig_level, use_container_width=True)

# ---------------------- Footer Description ----------------------
st.markdown("---")
st.caption("ACC102 Track4 | Air Quality Analysis Tool")


