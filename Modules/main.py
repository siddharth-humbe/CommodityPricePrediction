import pandas as pd
from data_collection import fetch_sugar_data
from data_preprocessing import preprocess_data, split_data, check_stationarity
from eda import plot_data, decompose_seasonality
from modeling import train_sarimax, forecast
from evaluation import calculate_metrics

# Fetch and preprocess data
url = 'https://www.indexmundi.com/commodities/?commodity=sugar&months=360'
df_raw = fetch_sugar_data(url)
df_processed = preprocess_data(df_raw)

# Split data into training and testing
df_train, df_test = split_data(df_processed)

# Perform EDA
plot_data(df_processed)
decompose_seasonality(df_processed)

# Train and forecast with SARIMAX
sarimax_model = train_sarimax(df_train, order=(11, 1, 11), seasonal_order=(1, 1, 1, 12))
sarima_forecast = forecast(sarimax_model, start=df_test.index[0], end=df_test.index[-1])

# Evaluate performance
metrics = calculate_metrics(df_test['price_cent'], sarima_forecast)
print(metrics)
