import ForexDataClient

c = ForexDataClient.ForexDataClient('jwP0y3RxNKOUDhcxbcwDQ79ASUCa51YE')

if c.marketIsOpen() == True:
    print("Open")

print(c.getSymbols())
