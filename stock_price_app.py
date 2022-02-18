import yfinance as yf
import streamlit as st

st.write("""
# Простое приложение для мониторинга цен акций с января 2016 по февраль 2022

Показывает цену открытия, закрытия и объем продаж Google
"""

)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#название компании
tickerSymbol = 'GOOGL'
#получаем данные
tickerData = yf.Ticker(tickerSymbol)
#получаем данные за период вермени по параметрам
tickerDf = tickerData.history(period='1d', start='2016-1-01', end='2022-2-17')
# Open	High	Low	Close	Volume	Dividends	Stock Splits  - что можем смотреть

st.write("""
## Цена открытия
""")
st.line_chart(tickerDf.Open)

st.write("""
## Цена закрытия
""")
st.line_chart(tickerDf.Close)

st.write("""
## Объем
""")
st.line_chart(tickerDf.Volume)
