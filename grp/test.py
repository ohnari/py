import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import sys
import requests
import json
from time import sleep

pairs = {
  'uj': 'USDJPY',
  'ej': 'EURJPY',
  'gj': 'GBPJPY',
  'aj': 'AUDJPY',
  'nj': 'NZDJPY',
  'cj': 'CADJPY',
  'eu': 'EURUSD',
  'gu': 'GBPUSD',
  'au': 'AUDUSD',
  'nu': 'NZDUSD',
  'uc': 'USDCAD',
  'ea': 'EURAUD'
}

url = "https://www.gaitameonline.com/rateaj/getrate"

def requestQuotes(argv, argc):
    res = ""
    api_data = requests.get(url).json()
    for i in range(argc - 1):
        for pair in api_data['quotes']:
            if pairs[argv[i+1]] == pair['currencyPairCode']:
                res += argv[i + 1] + " : " + pair['bid'] + "    "
    return res

def main():
    argv = sys.argv
    argc = len(argv)
    
    while True:
        plt.cla
        #x.append(frame)
        #y.append(frame)
        print(requestQuotes(argv, argc))
        sleep(60)
 
if __name__ == "__main__":
    main()
