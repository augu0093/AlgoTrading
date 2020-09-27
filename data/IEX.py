"""
Using IEX Cloud API to gather market data.
@AugustSemrau
"""
from keys.keyIEX import get_publishable_IEX_key
from keys.keyIEX import get_publishable_sandbox_IEX_key

import pandas as pd
import pyEX
from datetime import datetime

# Get API key from ignored filed..
# IEX_API_key = get_publishable_IEX_key()
IEX_API_key = get_publishable_sandbox_IEX_key()

p = pyEX.Client(IEX_API_key)
ticker = 'AMD'
timeframe = '1m'
df = p.chartDF(ticker, timeframe)
print(df.head())