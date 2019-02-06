#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
import sys
from time import sleep
import requests
import json
import NariPairs as na

url = "https://www.gaitameonline.com/rateaj/getrate"
numbers = ['GBPNZD', 'CADJPY', 'GBPAUD', 'AUDJPY', 'AUDNZD',    'EURCAD', 'EURUSD', 'NZDJPY', 'USDCAD',    'EURGBP', 'GBPUSD',
           'ZARJPY', 'EURCHF', 'CHFJPY', 'AUDUSD', 'USDCHF', 'EURJPY', 'GBPCHF', 'EURNZD', 'NZDUSD', 'USDJPY', 'EURAUD', 'AUDCHF', 'GBPJPY'
           ]


def main():
    sys.argv.pop(0)
    p = na.NariPairs(sys.argv)
    pairs = p.getSymbolList()
    #ay = np.empty([], dtype='f8')
    ay = ([])
    while True:
        api_data = requests.get(url).json()
        for pair in pairs:
            res = api_data['quotes'][numbers.index(pair)]['ask']
            ay=np.append(ay, res)
        sleep(5)
        print(ay)

if __name__ == '__main__':
    main()
