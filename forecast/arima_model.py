import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_mrr(df):
    model = ARIMA(df["mrr"], order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.predict(start=0, end=len(df)-1)
    return forecast
