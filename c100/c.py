import pandas as pd
import matplotlib.pyplot as plt
import datetime

PING_BASE = 'chg100'

def readCsv():
    data = pd.read_csv('c.csv', index_col='DATE')
    data['Total'] = data.sum(axis=1)
    return data


def myPlot(df, x):
    fig, ax1 = plt.subplots(figsize=(10, 4))
    ax1.set_xticklabels(x, rotation=90, size="small")
    plt.bar(df.index, df['Total'], label='Total', align='center')
    plt.legend(loc=4)

    ax2 = ax1.twinx()
    ax2.set_xticklabels(x, rotation=90, size="small")
    plt.plot(df.index, df['SBI'], 'b', label='S')
    plt.plot(df.index, df['GEM'], 'g', label='G')
    plt.plot(df.index, df['DOOM'], 'y', label='D')
    plt.legend()

    plt.savefig(PING_BASE + str(datetime.date.today()) + '.png')
    plt.show()


df = readCsv().iloc[:, [0, 1, 2, 3]]
#ax = list(readCsv().index)
ax = readCsv().columns
myPlot(df, ax)
