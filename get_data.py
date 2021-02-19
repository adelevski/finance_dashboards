from binance.client import Client
import config, csv


client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)


# csvfile = open('2018_2021.csv', 'w', newline='')
# candlestick_writer = csv.writer(csvfile, delimiter=',')


# candlestick = klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2018", "1 Jan, 2021")

# for candlestick in candlesticks:
#     candlestick_writer.writerow(candlestick)

# csvfile.close()
