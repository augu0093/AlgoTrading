"""
Using yfinance python package for attaining market data.
@AugustSemrau
"""

# import yfinance as yf


# # Stock
# symbol = 'MSFT'
#
# #get data on this ticker
# tickerData = yf.Ticker(symbol)
#
# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')
#
# #see your data
# tickerDf

import yfinance


msft = yfinance.download("MSFT")

# get stock info
msft.info()