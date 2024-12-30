from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax(df_train, order, seasonal_order=None):
    model = SARIMAX(df_train['price_cent'], order=order, seasonal_order=seasonal_order)
    model_fit = model.fit()
    return model_fit

def forecast(model_fit, start, end):
    forecast = model_fit.predict(start=start, end=end, dynamic=True)
    return forecast