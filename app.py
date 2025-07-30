import streamlit as st
import pandas as pd
import plotly.express as px
from forecast.arima_model import forecast_mrr
from alerts.anomaly_detection import detect_anomalies

st.set_page_config(page_title="SaaS KPI Dashboard", layout="wide")
st.title("📊 SaaS KPI Dashboard with Forecasting")

data = pd.read_csv("data/processed_netflix.csv", parse_dates=["date"])

data["forecast"] = forecast_mrr(data)
data["anomaly"] = detect_anomalies(data["active_users"])

col1, col2 = st.columns(2)
with col1:
    st.subheader("Monthly Recurring Revenue (MRR) Forecast")
    fig = px.line(data, x="date", y=["mrr", "forecast"], title="MRR and Forecast")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Active Users & Anomalies")
    fig = px.line(data, x="date", y="active_users", title="Active Users Over Time")
    fig.add_scatter(
        x=data['date'],
        y=data['active_users'].where(data['anomaly']),
        mode='markers',
        marker=dict(color='red', size=8),
        name='Anomalies'
    )
    st.plotly_chart(fig, use_container_width=True)
