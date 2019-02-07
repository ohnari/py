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
import talib as ta
#from tkinter import *
#from tkinter import ttk
import tkinter as Tk

url = "https://www.gaitameonline.com/rateaj/getrate"
numbers = ['GBPNZD', 'CADJPY', 'GBPAUD', 'AUDJPY', 'AUDNZD',    'EURCAD', 'EURUSD', 'NZDJPY', 'USDCAD',    'EURGBP', 'GBPUSD',
           'ZARJPY', 'EURCHF', 'CHFJPY', 'AUDUSD', 'USDCHF', 'EURJPY', 'GBPCHF', 'EURNZD', 'NZDUSD', 'USDJPY', 'EURAUD', 'AUDCHF', 'GBPJPY'
           ]


class Quotes():
    def __init__(self, p):
        self.pairs = p
        self.quote = np.array([])

    def getQuote(self):
        api_data = requests.get(url).json()
        for pair in self.pairs:
            res = api_data['quotes'][numbers.index(pair)]['ask']
        self.quote = np.append(self.quote, float(res))
        ema = ta.EMA(self.quote, timeperiod=26)
        src = '{:.4f}'.format(self.quote[-1])
        ma = '{:.4f}'.format(ema[-1])
        enq = '<' if(src <= ma) else '>'
        res = '{x} {y} {z}'.format(x=src, y=enq, z=ma)
        return res


class Application(Tk.Frame):
    def __init__(self, pairs, master=None):
        Tk.Frame.__init__(self, master)
        self.pack()
        self.pairs = Quotes(pairs)
        self.master = master
        self.master.title(pairs[0])
        self.create_widgets()

    def create_widgets(self):
        self.strval = Tk.StringVar()
        self.label = Tk.Label(self, textvariable=self.strval)
        self.label.grid(column=0, row=0)
        self.strval.set(self.pairs.getQuote())
        self.update_Quote()

    def update_Quote(self):
        self.strval.set(self.pairs.getQuote())
        self.master.after(6000, self.update_Quote)


def main():
    sys.argv.pop(0)
    if len(sys.argv) != 1:
        exit

    p = na.NariPairs(sys.argv)
    pairs = p.getSymbolList()

    root = Tk.Tk()
    app = Application(pairs, master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
