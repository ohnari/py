import requests
import urllib3
import json

MY_KEY = 'jwP0y3RxNKOUDhcxbcwDQ79ASUCa51YE'


class ForexDataClient:
    def __init__(self, api_key=MY_KEY):
        self.api_key = api_key
        self.base_uri = 'https://forex.1forge.com/1.0.3/'

    def fetch(self, uri):
        res = requests.get(self.base_uri + uri +
                           '&api_key=' + self.api_key).json()
        return res
        # https://forex.1forge.com/1.0.3/quotes?pairs=EURJPY,EURJPY&api_key=jwP0y3RxNKOUDhcxbcwDQ79ASUCa51YE

    def quota(self):
        return self.fetch('quota?cache=false')

    def getSymbols(self):
        return self.fetch('symbols?cache=false')

    def getQuotes(self, pairs):
        quotes = {}
        dt = self.fetch('quotes?pairs=' + ','.join(pairs))
        for idx, pair in enumerate(pairs):
            dic = dict(ask=dt[idx]['ask'], bid=dt[idx]
                       ['bid'], symbol=dt[idx]['symbol'])
            quotes[pair] = dic
        return quotes

    def marketIsOpen(self):
        data = self.fetch('market_status?cache=false')
        try:
            return data['market_is_open']
        except:
            print(data)

    def convert(self, currency_from, currency_to, quantity):
        return self.fetch('convert?from=' + currency_from + '&to=' + currency_to + '&quantity=' + str(quantity))
