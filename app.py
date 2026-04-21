import streamlit as st
import pandas as pd
import plotly.express as px

# 页面设置
st.set_page_config(page_title="Air Quality Tool", layout="wide")
st.title("🌬️ 空气质量分析工具 (ACC102 Track4)")

# 上传数据
uploaded_file = st.file_uploader("请上传你的空气质量CSV数据文件", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 数据加载成功！")
    st.subheader("<span class="emoji emoji1f4c8"></span> 数据预览")
    st.dataframe(df.head(10), use_container_width=True)
    
    # 基础统计
    st.subheader("<span class="emoji emoji1f4c8"></span> 数据概览")
    col1, col2, col3 = st.columns(3)
    if "AQI" in df.columns: 
        col1.metric("平均AQI", round(df["AQI"].mean(), 1))
        col2.metric("最高AQI", df["AQI"].max())
        col3.metric("最低AQI", df["AQI"].min())
  
   # 趋势图
   if "Date" in df.columns and "AQI" in df.columns:
       st.subheader("📉 AQI时间趋势")
       df["Date"] = pd.to_datetime(df["Date"])
       fig = px.line(df, x="Date", y="AQI", title="AQI随时间变化趋势")
       st.plotly_chart(fig, use_container_width=True)
else:
    st.info("ℹ️ 请上传CSV文件，开始你的空气质量分析！")
