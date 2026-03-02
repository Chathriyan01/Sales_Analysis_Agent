import streamlit as st
import pandas as pd
from modules.data_loader import load_sales_data
from modules.visualizer import sales_over_time, sales_by_region, category_distribution
from modules.forecasting import train_forecast_model, forecast_sales
from modules.utils import format_number

st.set_page_config(page_title="Sales Analyzing Agent", layout="wide")
st.sidebar.image("./assets/company_logo.png", width=200)
st.sidebar.title("Sales Analyzing Agent")

df = load_sales_data("./data/sales_data.csv")

st.title("Sales Dashboard with Forecasting")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", format_number(df["sales"].sum()))
col2.metric("Average Daily Sales", format_number(df["sales"].mean()))
col3.metric("Max Sale", format_number(df["sales"].max()))

st.subheader("Sales Trend Over Time")
st.plotly_chart(sales_over_time(df), use_container_width=True)

st.subheader("Sales by Region")
st.plotly_chart(sales_by_region(df), use_container_width=True)

st.subheader("Category Contribution")
st.plotly_chart(category_distribution(df), use_container_width=True)

st.header("Sales Forecasting")
periods = st.slider("Days to Forecast:", 7, 180, 30)

model = train_forecast_model(df)
forecast = forecast_sales(model, periods)

st.subheader("Forecast Plot")
forecast_fig = forecast[["ds","yhat"]].rename(columns={"ds":"Date","yhat":"Predicted Sales"})
st.line_chart(forecast_fig.set_index("Date"))

st.subheader("Forecast Data")
st.dataframe(forecast[["ds","yhat","yhat_lower","yhat_upper"]].tail(periods))
