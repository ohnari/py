#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib import animation
import sys
from lib import NariPairs
import ForexDataClient

xlim = [0, 180]


def _update(frame, x, y, pairs, ax):
    """グラフを更新するための関数"""
    plt.cla()
    t = ForexDataClient.ForexDataClient().getQuotes(pairs)
    for i, j in enumerate(t):
        y[i].append(j['ask'])
    x.append(len(y[0]))
    if len(x) > 180:  # 描画範囲を更新
        xlim[0] += 1
        xlim[1] += 1
    for i, j in enumerate(pairs):
        ax[i].plot(x, y[i], color='b')
        ax[i].set_xlim(xlim[0], xlim[1])
        ax[i].set_title(
            NariPairs.NariPairs(pairs).getCode(j), loc='right', size=10)
        ax[i].tick_params(labelbottom=False)


def main():
    ax = []
    x = []
    y = []

    sys.argv.pop(0)
    p = NariPairs.NariPairs(sys.argv)
    pairs = p.getSymbolList()
    if (len(pairs) < 1):
        sys.exit()

    fig = plt.figure(figsize=(5, len(pairs) * 2))
    fig.subplots_adjust(top=0.96, hspace=0.2)
    for j in range(len(pairs)):
        ax.append(fig.add_subplot(len(pairs), 1, j + 1))
        y.append([])

    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'fargs': (x, y, pairs, ax),  # 関数の引数 (フレーム番号を除く)
        'interval': 60000,  # 更新間隔 (ミリ秒)
        'repeat': False,  # 繰り返さない
    }
    anime = animation.FuncAnimation(**params)
    plt.show()


if __name__ == '__main__':
    main()
