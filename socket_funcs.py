import json
import streamlit as st

def on_open(ws):
    st.write("opened connection")

    request = {
        "method": "SUBSCRIBE",
        "params": [
            "btcusdt@aggTrade",
            "ethusdt@aggTrade"
        ],
        "id": 1
    }    

    ws.send(json.dumps(request))

def on_message(ws, message):
    data = json.loads(message)
    price = data['p']
    message_handler(price)

def on_close(ws):
    message_handler('closed connection')