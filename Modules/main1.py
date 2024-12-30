from modeling import train_sarimax, forecast, save_model

# Train the model
sarimax_model = train_sarimax(df_train, order=(11, 1, 11), seasonal_order=(1, 1, 1, 12))

# Save the trained model to a pickle file
save_model(sarimax_model, "sarimax_model.pkl")

# Forecast using the trained model
sarima_forecast = forecast(sarimax_model, start=df_test.index[0], end=df_test.index[-1])