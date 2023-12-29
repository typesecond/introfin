import requests
import yfinance as yf

tsla = yf.Ticker("TSLA")
hist = tsla.history(period="1mo")
print(tsla.info)



print(tsla.quarterly_income_stmt)
print(tsla.mutualfund_holders)
print(tsla.cash_flow)
#hedge pop? 