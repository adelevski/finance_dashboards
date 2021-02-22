from binance.client import Client
import config, csv


client = Client(config.API_KEY, config.API_SECRET)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)


csvfile = open('daily.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')


candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Nov, 2020", "20 Feb, 2021")

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()
