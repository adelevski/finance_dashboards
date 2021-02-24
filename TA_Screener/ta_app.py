import os, csv
import pandas as pd
import talib
from flask import Flask, render_template, request
from patterns import patterns
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    pattern = request.args.get('pattern', None)
    stocks = {}

    with open('datasets/companies.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}



    if pattern:
        datafiles = os.listdir('TA_Screener/data/daily')
        for filename in datafiles:
            df = pd.read_csv(f'TA_Screener/data/daily/{filename}')
            pattern_function = getattr(talib, pattern)
            symbol = filename.split('.')[0]
            try:
                result = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                last = result.tail(1).values[0]
                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None
            except:
                pass
    return render_template('ta_index.html', patterns=patterns, stocks=stocks, current_pattern=pattern)

@app.route('/snapshot')
def snapshot():
    # with open('TA_Screener\datasets\companies.csv') as f:
    #     companies = f.read().splitlines()
    #     for company in companies:
    #         symbol = company.split(',')[0]
    #         df = yf.download(symbol, start="2020-06-22", end="2021-02-22")
    #         df.to_csv(f'TA_Screener\datas\daily\{symbol}.csv')

    return {
        'code': "success"
    }