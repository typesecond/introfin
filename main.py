import requests
import yfinance as yf

tsla = yf.Ticker("TSLA")

print(tsla.info)