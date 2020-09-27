"""
Using Alpaca API for attaining market data.
@AugustSemrau
"""

from keys.keyAlpaca import get_publishable_Alpaca_key
from keys.keyAlpaca import get_secret_Alpaca_key
import alpaca_trade_api as tradeapi
import time

key = get_publishable_Alpaca_key()
sec = get_secret_Alpaca_key()

# Endpoint URL
url = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(key, sec, url, api_version='v2')

#Init our account var
account = api.get_account()

print(account.status)