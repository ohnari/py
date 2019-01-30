#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import sys
import requests
import json

url = "https://www.gaitameonline.com/rateaj/getrate"
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
xlim = [0, 100]

def requestQuotes(p):
    api_data = requests.get(url).json()
    for pair in api_data['quotes']:
        if pairs[p] == pair['currencyPairCode']:
          res = pair['bid']
    return res


def _update(frame, x, y1, y2, pair1, pair2, ax1, ax2):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # データを更新 (追加) する
    y1.append(float(requestQuotes(pair1)))
    y2.append(float(requestQuotes(pair2)))
    x.append(len(y1))
    # 折れ線グラフを再描画する
    if len(x) > 100:            # 描画範囲を更新
        xlim[0] += 1
        xlim[1] += 1
    #plt.plot(x, y1)
    #plt.plot(x, y2)
    ax1.plot(x, y1, marker = 'x')
    ax2.plot(x, y2, marker = 'o')
    plt.xlim(xlim[0], xlim[1])

def main():
    pair1 = sys.argv[1]
    pair2 = sys.argv[2]
    # 描画領域
    fig = plt.figure(figsize=(5, 3))
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()
    # 描画するデータ (最初は空っぽ)
    x = []
    y1 = []
    y2 = []

    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'fargs': (x, y1, y2, pair1, pair2, ax1, ax2),  # 関数の引数 (フレーム番号を除く)
        'interval': 60000,  # 更新間隔 (ミリ秒)
        #'frames': np.arange(0, 10, 0.1),  # フレーム番号を生成するイテレータ
        'repeat': False,  # 繰り返さない
    }
    anime = animation.FuncAnimation(**params)

    # グラフを表示する
    plt.show()


if __name__ == '__main__':
    main()
