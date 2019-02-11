#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import GaitameDataClient as gdc
import NariPairs as na
import talib as ta
import tkinter as Tk


PERIOD_MA = 26
INTERVAL = 60000
PERIOD_RCI = 9


class Quotes():
    def __init__(self, p):
        self.pairs = p
        self.quote = np.array([[] for i in range(len(p))])
        self.gd = gdc.GaitameDataClient()

    def getQuote(self):
        res = [[] for i in range(len(self.pairs))]
        t = []
        api_data = self.gd.getQuotes(self.pairs)
        for i, pair in enumerate(self.pairs):
            res[i].append(api_data[pair]['ask'])
        self.quote = np.append(self.quote, res, axis=1)
        for i in range(len(self.pairs)):
            ema = ta.SMA(self.quote[i], timeperiod=PERIOD_MA)
            src = '{:.4f}'.format(self.quote[i][-1])
            ma = '{:.4f}'.format(ema[-1])
            enq = '<' if(src <= ma) else '>'
            t.append('{x} {y} {z}'.format(x=src, y=enq, z=ma))
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
        self.master.after(300000, self.update_Quote)


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
