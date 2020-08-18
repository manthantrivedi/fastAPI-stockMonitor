import yfinance as yf

msft = yf.Ticker("MSFT")

#get stock Info
print(msft.info)