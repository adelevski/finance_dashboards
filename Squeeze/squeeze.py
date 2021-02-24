import os
import yfinance as yf
import pandas as pd

for filename in os.listdir("datasets/daily"):
    # symbol = filename.split(".")[0]
    df = pd.read_csv(f'datasets/daily/{filename}')