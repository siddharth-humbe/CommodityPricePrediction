import matplotlib.pyplot as plt

def plot_data(df):
    df.plot(subplots=True, figsize=(10, 12))
    plt.show()

def plot_price_change(df):
    plt.figure(figsize=(10, 6))
    df['price_diff'] = df['price'].diff(2)
    df['price_diff'].plot()
    plt.title("Price Difference")
    plt.show()

    df['change_diff'] = df['change'].diff(2)
    df['change_diff'].plot()
    plt.title("Change Difference")
    plt.show()

def decompose_seasonality(df):
    from statsmodels.tsa.seasonal import seasonal_decompose
    decomposition = seasonal_decompose(df['price_cent'], model="additive")
    decomposition.plot()
    plt.show()