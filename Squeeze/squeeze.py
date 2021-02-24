import os
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

symbols = ['AAPL']

for filename in os.listdir("datasets/daily"):
    symbol = filename.split(".")[0]
    df = pd.read_csv(f'datasets/daily/{filename}')
    if df.empty:
        continue

    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['std'] = df['Close'].rolling(window=20).std()
    df['lowerband'] = df['20sma'] - (2 * df['std'])
    df['upperband'] = df['20sma'] + (2 * df['std'])

    df['TR'] = abs(df['High']-df['Low'])
    df['ATR'] = df['TR'].rolling(window=20).mean()

    df['upperKC'] = df['20sma'] + (df['ATR'] * 1.5)
    df['lowerKC'] = df['20sma'] - (df['ATR'] * 1.5)

    def in_squeeze(df):
        return df['lowerband']>df['lowerKC'] and df['upperband']<df['upperKC']

    df['squeeze_on'] = df.apply(in_squeeze, axis=1)

    if df.iloc[-3]['squeeze_on'] and not df.iloc[-1]['squeeze_on']:
        print(f"{symbol} is coming out of the squeeze")


    # if symbol in symbols:
    #     aapl_df = df

# candlestick = go.Candlestick(x=aapl_df['Date'], open=aapl_df['Open'], high=aapl_df['High'], low=aapl_df['Low'], close=aapl_df['Close'])
# upperband = go.Scatter(x=aapl_df['Date'], y=aapl_df['upperband'], name='Upper Bollinger Band', line={'color': 'orange'})
# lowerband = go.Scatter(x=aapl_df['Date'], y=aapl_df['lowerband'], name='Lower Bollinger Band', line={'color': 'orange'})
# upperKC = go.Scatter(x=aapl_df['Date'], y=aapl_df['upperKC'], name='Upper Keltner Channel', line={'color': 'blue'})
# lowerKC = go.Scatter(x=aapl_df['Date'], y=aapl_df['lowerKC'], name='Lower Keltner Channel', line={'color': 'blue'})

# fig = go.Figure(data=[candlestick, upperband, lowerband, upperKC, lowerKC])
# fig.layout.xaxis.type = 'category'
# fig.layout.xaxis.rangeslider.visible = False

# fig.show()

