import datetime
import json
import sys
from datetime import datetime, timedelta

import pandas as pd
import pytz

import account as ac
import common as oc
from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingInfo
from oandapyV20.endpoints.instruments import InstrumentsCandles
from oandapyV20.exceptions import V20Error
from pack import NariPairs as nari

COUNT = 1650


class OandaDataClient():

    def __init__(self, nari_code):
        a = nari.getOandaSymbolList(nari_code)
        *params, = [{
            "count": 50,
            "granularity": oc.OANDA_GRN.M1
        }, {
            "instruments": ','.join(a)
        }]
        self.__api = API(access_token=ac.access_token,
                         environment=oc.OANDA_ENV.PRACTICE)

        self.__Candles = InstrumentsCandles(a[0], params[0])
        self.__Info = PricingInfo(ac.account_ID, params[1])

    def pastCandles(self):
        data = []
        r = self.__api.request(self.__Candles)
        for raw in r['candles']:
            data.append([raw['mid']['c']])
        df = pd.DataFrame(data)
        df.columns = ['close']
        return(df)


def main():
    sys.argv.pop(0)
    if len(sys.argv) != 1:
        exit
    odc = OandaDataClient(sys.argv)
    a = odc.pastCandles()
    print(a)


if __name__ == '__main__':
    main()
