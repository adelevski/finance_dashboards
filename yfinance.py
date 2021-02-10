import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Ticker Load')

tickerSymbol = st.sidebar.text_input("Ticker?")
period = st.sidebar.selectbox("Period?", ('1d','5d','1mo','3mo','6mo',
                                            '1y','2y', '5y', '10y', 'ytd', 'max'))


if tickerSymbol:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period=period)

    st.write(tickerSymbol + ' Close')
    st.line_chart(tickerDf.Close)

    st.write(tickerSymbol + ' Volume')
    st.bar_chart(tickerDf.Volume)
else:
    pass


