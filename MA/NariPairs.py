
NariPairsList = {
    'uj': {'code': 'uj', 'symbol': 'USDJPY', 'fdig': 3},
    'ej': {'code': 'ej', 'symbol': 'EURJPY', 'fdig': 3},
    'gj': {'code': 'gj', 'symbol': 'GBPJPY', 'fdig': 3},
    'aj': {'code': 'aj', 'symbol': 'AUDJPY', 'fdig': 3},
    'nj': {'code': 'nj', 'symbol': 'NZDJPY', 'fdig': 3},
    'cj': {'code': 'cj', 'symbol': 'CADJPY', 'fdig': 3},
    'eu': {'code': 'eu', 'symbol': 'EURUSD', 'fdig': 5},
    'gu': {'code': 'gu', 'symbol': 'GBPUSD', 'fdig': 5},
    'au': {'code': 'au', 'symbol': 'AUDUSD', 'fdig': 5},
    'nu': {'code': 'nu', 'symbol': 'NZDUSD', 'fdig': 5},
    'uc': {'code': 'uc', 'symbol': 'USDCAD', 'fdig': 5},
    'ea': {'code': 'ea', 'symbol': 'EURAUD', 'fdig': 5},
    'eg': {'code': 'eg', 'symbol': 'EURGBP', 'fdig': 5},
}


class NariPairs:
    def __init__(self, pairs):
        self.symbol = []
        self.oanda_symbol = []
        for x in pairs:
            y = NariPairsList[x]['symbol']
            tmp = '{0}{1}{2}'.format(y[:3], '_', y[3:])
            self.symbol.append(y)
            self.oanda_symbol.append(tmp)

    def getOandaSymbolList(self):
        return self.oanda_symbol

    def getSymbolList(self):
        return self.symbol

    def getFdig(self, symbol):
        for x in NariPairsList:
            if x['symbol'] == symbol:
                return(x['fdig'])
        return (-1)
