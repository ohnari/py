import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime
import requests
import json
import numpy as np
import talib


def get_bit():
    url = ('https://api.coingecko.com/api/v3/coins/') + \
        str('bitcoin')+('/market_chart?vs_currency=jpy&days=max')
    r = requests.get(url)
    r = json.loads(r.text)
    bitcoin = r['prices']
    data = []
    date = []
    for i in bitcoin:
        data.append(i[1])
        date.append(i[0])
        bit = pd.DataFrame({"date": date, "price": data})
        price = bit['price']
        change = price.pct_change()
        bit = pd.DataFrame({"date": date, "price": data, "change": change})
    return bit


b = get_bit()
p = b['price']
p = np.array(p)
print(p)
print(talib.EMA(p, timeperiod=2)[-1])
