from config import ameritrade
import websocket, json
from websocket import create_connection, WebSocket
import requests, time, re
import pandas as pd
import streamlit as st
import pprint

st.title("QuickTick")


start_button = st.empty()
placeholder = st.empty()

def on_open(ws):
    st.write("opened connection")

    request = {
        "method": "SUBSCRIBE",
        "params": [
            "btcusdt@trade"
        ],
        "id": 1
    }    

    ws.send(json.dumps(request))

def on_message(ws, message):
    print_message(message)


def print_message(message):
    data = json.loads(message)
    symbol = data['s']
    price = data['p']
    placeholder.write(data)

def on_close(ws):
    st.write('closed connection')

endpoint = 'wss://stream.binance.com:9443/ws'
ws = websocket.WebSocketApp(endpoint, on_close=on_close, on_open=on_open, on_message=on_message)

if start_button.button('Start',key='start'):
    start_button.empty()
    if st.button('Stop',key='stop'):
        pass
    while True:
        ws.run_forever()
ws.close()


# tickerSymbol = st.sidebar.text_input("Ticker?")

# while tickerSymbol:
#     st.write(data)
#     # tickerData = yf.Ticker(tickerSymbol)
#     # tickerDf = tickerData.history(period=period)

#     # st.write(tickerSymbol + ' Close')
#     # st.line_chart(tickerDf.Close)

#     # st.write(tickerSymbol + ' Volume')
#     # st.bar_chart(tickerDf.Volume)
#     time.sleep(1)
# else:
#     pass