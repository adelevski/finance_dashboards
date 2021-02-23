from flask import Flask, render_template
from patterns import patterns
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ta_index.html', patterns=patterns)

@app.route('/snapshot')
def snapshot():
    # with open('TA_Screener\datasets\companies.csv') as f:
    #     companies = f.read().splitlines()
    #     for company in companies:
    #         symbol = company.split(',')[0]
    #         df = yf.download(symbol, start="2020-06-22", end="2021-02-22")
    #         df.to_csv(f'TA_Screener\datasets\daily\{symbol}.csv')

    return {
        'code': "success"
    }