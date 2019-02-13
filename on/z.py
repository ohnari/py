#from pack import NariPairs
#from pack import ForexDataClient
#from pack import GaitameDataClient
#from pack import NariPairs
import pack

p = pack.NariPairs.getSymbolList(['eu'])
a = pack.GaitameDataClient()
b = pack.ForexDataClient()
c = a.getQuotes(p)
print(c)
print(b.base_uri)
