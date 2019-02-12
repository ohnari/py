import requests as req

URI = "https://www.gaitameonline.com/rateaj/getrate"


class GaitameDataClient:
    def __init__(self):
        pass

    def __pairIndex(self, data):
        pair_no = {}
        for idx, pair in enumerate(data):
            pair_no.update([(pair['currencyPairCode'], idx)])
        return pair_no

    def getQuotes(self, pairs):
        quotes = {}
        api_data = req.get(URI).json()['quotes']
        pair_no = self.__pairIndex(api_data)
        for pair in pairs:
            dt = api_data[pair_no[pair]]
            dic = dict(ask=float(dt['ask']), bid=float(dt['bid']),
                       symbol=dt['currencyPairCode'])
            quotes[pair] = dic
        return quotes
