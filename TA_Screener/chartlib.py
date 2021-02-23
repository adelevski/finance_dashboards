import os
import pandas as pd


def is_consolidating(df, percentage=2):
    recent_candlesticks = df[-30:-15]

    max_close = recent_candlesticks['Close'].max()
    min_close = recent_candlesticks['Close'].min()
    threshold = 1 - percentage/100
    if min_close > (max_close * threshold):
        return True
        

def is_breaking_out(df):
    pass






datafiles = os.listdir('TA_Screener/datasets/daily')
for filename in datafiles:
    df = pd.read_csv(f'TA_Screener/datasets/daily/{filename}')

    if is_consolidating(df, percentage=2.5):
        print(f"{filename} is consolidating.")
