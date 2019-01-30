import pandas as pd
import matplotlib.pyplot as plt
import datetime

PING_BASE = 'chg100'


def readCsv():
    data = pd.read_csv('c.csv', index_col='DATE')
    data['S'] = data['S_'] - data['S_F']
    data['G'] = data['G_'] - data['G_F']
    data['D'] = data['D_'] - data['D_F']
    data['T'] = data[['S', 'G', 'D']].sum(axis=1)
    return data


def myPlot(df, x):
    fig, ax1 = plt.subplots(figsize=(10, 4))
    ax1.set_xticklabels(x, rotation=90, size="small")
    plt.bar(df.index, df['T'], label='Total', align='center')
    plt.legend(loc=4)

    ax2 = ax1.twinx()
    ax2.set_xticklabels(x, rotation=90, size="small")
    plt.plot(df.index, df['S'], 'b', label='S')
    plt.plot(df.index, df['G'], 'g', label='G')
    plt.plot(df.index, df['D'], 'y', label='D')
    plt.legend()

    title = "{:,}".format(df.iloc[-1]['T'])
    plt.title(title)
    plt.savefig(PING_BASE + str(datetime.date.today()) + '.png')
    plt.show()


df = readCsv().loc[:, ['S', 'G', 'D', 'T']]
ax = readCsv().index
myPlot(df, ax)
