import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------- 页面基础设置 ----------------------
st.set_page_config(
    page_title="Air Quality Tool | ACC102 Track4",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 标题与简介
st.title("🌬️ 空气质量分析工具 (ACC102 Track4)")
st.markdown("这是一个交互式空气质量数据分析工具，支持数据预览、趋势分析与污染物对比。")

# ---------------------- 读取数据 ----------------------
# 读取你上传到仓库的CSV文件
df = pd.read_csv("air_quality.csv")
df["Date"] = pd.to_datetime(df["Date"])  # 转换日期格式

# ---------------------- 侧边栏筛选器 ----------------------
st.sidebar.header("筛选设置")

# 城市筛选
city_list = df["City"].unique()
selected_cities = st.sidebar.multiselect(
    "选择城市",
    options=city_list,
    default=city_list[0]
)

# 日期范围筛选
min_date = df["Date"].min()
max_date = df["Date"].max()
selected_dates = st.sidebar.date_input(
    "选择时间范围",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# 应用筛选条件
filtered_df = df[
(df["City"].isin(selected_cities)) &
(df["Date"] >= pd.to_datetime(selected_dates[0])) &
(df["Date"] <= pd.to_datetime(selected_dates[1]))
]

# ---------------------- 数据概览 ----------------------
st.subheader("<span class="emoji emoji1f4c8"></span> 数据概览")

# 关键指标卡片
col1, col2, col3 = st.columns(3)
col1.metric("平均AQI", round(filtered_df["AQI"].mean(), 1))
col2.metric("最高AQI", filtered_df["AQI"].max())
col3.metric("最低AQI", filtered_df["AQI"].min())

# 数据预览
st.dataframe(filtered_df, use_container_width=True)

# ---------------------- 可视化图表 ----------------------
# 1. AQI时间趋势图
st.subheader("<span class="emoji emoji1f4c8"></span> AQI 时间变化趋势")
fig_aqi = px.line(
filtered_df,
x="Date",
y="AQI",
color="City",
title="不同城市AQI随时间变化趋势",
labels={"AQI": "空气质量指数(AQI)", "Date": "日期"}
)
st.plotly_chart(fig_aqi, use_container_width=True)

# 2. 污染物浓度对比
st.subheader("<span class="emoji emoji1f3ed"></span> 主要污染物平均浓度对比")
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "O3"]
avg_pollutants = filtered_df.groupby("City")[pollutants].mean().reset_index()
fig_pollutants = px.bar(
avg_pollutants,
x="City",
y=pollutants,
barmode="group",
title="不同城市主要污染物平均浓度"
)
st.plotly_chart(fig_pollutants, use_container_width=True)

# 3. 空气质量等级分布
st.subheader("<span class="emoji emoji1f3af"></span> 空气质量等级分布")
fig_level = px.pie(
filtered_df,
names="Quality_Level",
title="空气质量等级占比分布",
hole=0.3
)
st.plotly_chart(fig_level, use_container_width=True)

# ---------------------- 页脚说明 ----------------------
st.markdown("---")
st.caption("ACC102 Track4 作业 | 空气质量分析工具")

