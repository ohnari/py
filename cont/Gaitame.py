#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import NariPairs
import sys
import requests
import json

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


class Gatame:
    def __init__(self, pair):
        self.api_data = None

    def requestQuotes(p):
        self.api_data = requests.get(url).json()
        for pair in api_data['quotes']:
            if pairs[p] == pair['currencyPairCode']:
            res = pair['bid']
        return res

