import requests
import yfinance as yf

tsla = yf.Ticker("TSLA")
hist = tsla.history(period="1mo")
print(tsla.info)



print(tsla.quarterly_income_stmt)
print(tsla.mutualfund_holders)
print(tsla.cash_flow)
#hedge pop? 
hol = tsla.earnings_dates
# jj intel
print(hol) 
# spread soon
# buttefly implementation
# spread work? 
nol = tsla.actions
tol = tsla.calendar
sol = tsla.fast_info
# wait delt hold