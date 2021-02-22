import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('15minute.csv', delimiter=',')

close = my_data[:, 4]

print(close)

# moving_average = talib.SMA(close, timeperiod=10)

# print(moving_average)

rsi = talib.RSI(close)

print(rsi)