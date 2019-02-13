import json
import sys

import account as ac
import common as oc
from pack import NariPairs as nari
from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingInfo
from oandapyV20.exceptions import V20Error


class OandaDataClient():
    def __init__(self, nari_code):
        a = nari.getOandaSymbolList(nari_code)
        self.__api = API(access_token=ac.access_token,
                         environment=oc.OANDA_ENV.PRACTICE)
        params = {"instruments": ','.join(a)}
        self.__pinfo = PricingInfo(ac.account_ID, params)
        self.code = nari.getSymbolList(nari_code)

    def getQuotes(self):
        try:
            quotes = {}
            for i, r in enumerate(self.__api.request(self.__pinfo)['prices']):
                dic = dict(ask=float(r["asks"][0]["price"]),
                           bid=float(r["bids"][0]["price"]),
                           symbol=r['instrument'])
                quotes[self.code[i]] = dic
            return(quotes)
        except V20Error as e:
            return("Error: {}".format(e))


def main():
    sys.argv.pop(0)
    if len(sys.argv) != 1:
        exit
    odc = OandaDataClient(sys.argv)
    a = odc.getQuotes()
    print(a)


if __name__ == '__main__':
    main()
