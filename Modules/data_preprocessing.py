import pandas as pd
from pandas.tseries.offsets import DateOffset

def preprocess_data(df):
    df = df[1:].copy()
    df['price'] = df['price'].astype(float)
    df['change'] = df['change'].str.rstrip('%').astype('float')
    df['month'] = pd.to_datetime(df['month'])
    df['price_cent'] = df['price'] * 100  # Convert to cents
    return df

def split_data(df, train_date="2019-01-01"):
    df_train = df[df.index < pd.to_datetime(train_date)]
    df_test = df[df.index >= pd.to_datetime(train_date)]
    return df_train, df_test

def check_stationarity(df):
    rolling_mean = df.rolling(window=12).mean()
    return rolling_mean - rolling_mean.shift()

def add_time_features(df):
    df['price_diff'] = df['price'].diff()
    df['price_ratio'] = df['price'] / df['price'].shift()
    return df