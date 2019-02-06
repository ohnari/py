
NariPairsList = [
    {'code': 'uj', 'symbol': 'USDJPY', 'fdig': 3},
    {'code': 'ej', 'symbol': 'EURJPY', 'fdig': 3},
    {'code': 'gj', 'symbol': 'GBPJPY', 'fdig': 3},
    {'code': 'aj', 'symbol': 'AUDJPY', 'fdig': 3},
    {'code': 'nj', 'symbol': 'NZDJPY', 'fdig': 3},
    {'code': 'cj', 'symbol': 'CADJPY', 'fdig': 3},
    {'code': 'eu', 'symbol': 'EURUSD', 'fdig': 5},
    {'code': 'gu', 'symbol': 'GBPUSD', 'fdig': 5},
    {'code': 'au', 'symbol': 'AUDUSD', 'fdig': 5},
    {'code': 'nu', 'symbol': 'NZDUSD', 'fdig': 5},
    {'code': 'uc', 'symbol': 'USDCAD', 'fdig': 5},
    {'code': 'ea', 'symbol': 'EURAUD', 'fdig': 5},
    {'code': 'eg', 'symbol': 'EURGBP', 'fdig': 5},
]

class NariPairs:
    def __init__(self, pairs):
        self.codes = []
        self.symbols = []
        for x in pairs:
            for y in NariPairsList:
                if (y['code'] == x.lower()):
                    self.codes.append(x.lower())
                    self.symbols.append(y['symbol'])

    def getCodeList(self):
        return self.codes

    def getSymbolList(self):
        return self.symbols

    def getCode(self, symbol):
        for x in NariPairsList:
            if x['symbol'] == symbol:
                return(x['code'])
        return (None)

    def getFdig(self, symbol):
        for x in NariPairsList:
              if x['symbol'] == symbol:
                return(x['fdig'])
        return (-1)
