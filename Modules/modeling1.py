import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax(df_train, order, seasonal_order=None):
    model = SARIMAX(df_train['price_cent'], order=order, seasonal_order=seasonal_order)
    model_fit = model.fit()
    return model_fit

def save_model(model_fit, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model_fit, file)
    print(f"Model saved to {filename}")

def load_model(filename):
    with open(filename, 'rb') as file:
        model_fit = pickle.load(file)
    print(f"Model loaded from {filename}")
    return model_fit