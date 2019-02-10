#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import sys
import NariPairs as na
import ForexDataClient as fx
import talib as ta
import tkinter as Tk

PERIOD_MA = 26
INTERVAL = 10000
PERIOD_RCI = 9


class Quotes():
    def __init__(self, p):
        self.pairs = p
        self.quote = np.array([[] for i in range(len(p))])
        self.fx = fx.ForexDataClient()

    def getRci(self, seq, itv):
        # 時間帯の順位作成
        rank_period = np.arange(itv, 0, -1)

        length = len(seq)
        rci = np.zeros(length)

        for i in range(length):
            # rciの数合わせ、最初からperiod-1分は0にする
            if i < itv - 1:
                rci[i] = 0
            else:
                # 価格順位取得
                rank_price = pd.Series(
                    seq)[i - itv + 1: i + 1].rank(
                        method='min', ascending=False).values
                # rci(numpy)を取得
                rci[i] = (1 - (6 * sum((rank_period - rank_price)**2)) /
                          (itv**3 - itv)) * 100
        return rci[-1]

    def getQuote(self):
        res = [[] for i in range(len(self.pairs))]
        t = []
        for i, pair in enumerate(self.fx.getQuotes(self.pairs)):
            res[i].append(float(pair['ask']))
        self.quote = np.append(self.quote, res, axis=1)
        for i in range(len(self.pairs)):
            ema = ta.SMA(self.quote[i], timeperiod=PERIOD_MA)
            rci = '{:.4f}'.format(self.getRci(self.quote[i], PERIOD_RCI))
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
