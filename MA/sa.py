#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
from time import sleep
import requests
import json
import NariPairs as na
import ForexDataClient as fx
import talib as ta
import tkinter as Tk

PERIOD_MA = 26
INTERVAL = 1000
PERIOD_RCI = 9


class Quotes():
    def __init__(self, p):
        self.pairs = p
        self.quote = np.array([[] for i in range(len(p))])
        self.fx = fx.ForexDataClient()

    def Rci_o(self, seq, idx, itv):
        p = seq[idx]
        o = 1
        for i in range(itv - 1):
            if p < seq[i]:
                o += 1
        return o

    def Rci_d(self, seq, itv):
        d = 0
        for i in range(itv - 1):
            d += pow((i + 1) - self.Rci_o(seq, i, itv), 2)
        return d

    def Rci(self, seq, itv):
        sum = 0
        if (len(seq) >= itv):
            sum = (1-6*self.Rci_d(seq, itv) / (itv*(itv ** 2-1)))*100
        return sum

    def getQuote(self):
        res = [[] for i in range(len(self.pairs))]
        t = []
        for i, pair in enumerate(self.fx.getQuotes(self.pairs)):
            res[i].append(float(pair['ask']))
        self.quote = np.append(self.quote, res, axis=1)
        for i in range(len(self.pairs)):
            ema = ta.SMA(self.quote[i], timeperiod=PERIOD_MA)
            rci = self.Rci(self.quote[i], PERIOD_RCI)
            src = '{:.4f}'.format(self.quote[i][-1])
            ma = '{:.4f}'.format(ema[-1])
            enq = '<' if(src <= ma) else '>'
            t.append('{x} {y} {z} : {a}'.format(x=src, y=enq, z=ma, a=rci))
        print(t)
        return t


class Application(Tk.Frame):
    def __init__(self, pairs, master=None):
        Tk.Frame.__init__(self, master)
        self.pack()
        self.pairs = Quotes(pairs)
        self.master = master
        self.master.title('t_OO')
        self.create_widgets()

    def create_widgets(self):
        self.strval = Tk.StringVar()
        self.label = Tk.Label(self, textvariable=self.strval)
        self.label.grid(column=0, row=0)
        self.strval.set(self.pairs.getQuote())
        self.update_Quote()

    def update_Quote(self):
        self.strval.set(self.pairs.getQuote())
        self.master.after(INTERVAL, self.update_Quote)


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
