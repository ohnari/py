import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

PNG_BASE = '_chg100.png'
CSV_BASE = 'c.csv'
PairLabel = ['S', 'G', 'D', 'X']
PairColor = ['r', 'g', 'b', 'Y']
Index = 'DATE'
PathPub = 'G:\\マイドライブ\\c100\\'
# PathPub = 'C:\\Users\\onari.tetsuya\\Dropbox\\hellopy\\c100\\'
PathHome = '/home/nari/GoogleDrive/c100/'
# PathHome = '/home/nari/Dropbox/hellopy/c100/'


Path = PathPub if (os.path.exists(PathPub)) else PathHome
CsvFile = Path + CSV_BASE
PngFile = Path + str(datetime.date.today()) + PNG_BASE


class ReadCsv:
    def __init__(self, file):
        cols = [Index]
        for l in PairLabel:
            cols.append(l+'x')
            cols.append(l+'y')
        self.orgData = pd.read_csv(
            file, index_col=Index, skiprows=1, names=cols).dropna(how='any')
        self.data = pd.DataFrame(index=self.orgData.index, columns=PairLabel)

    def getOrgData(self):
        return self.orgData

    def getData(self):
        for i, j in enumerate(PairLabel):
            self.data[j] = self.orgData.iloc[:, i*2] - \
                self.orgData.iloc[:, i*2+1]
        self.data['T'] = self.data[PairLabel].sum(axis=1)
        return self.data

    def getResuData(self):
        return self.data.iloc[:, -len(PairLabel)-1:]

    def getIndex(self):
        return self.data.index

    def getColumns(self):
        return self.data.columns

    def getShape(self):
        return self.data.shape


def myPlot(df, x):
    t = []
    fig, ax1 = plt.subplots(figsize=(10, 4))

    ax1.set_xticklabels(x, rotation=90, size="small")
    lv = 'T:' + "{:,}".format(df.iloc[-1]['T'])
    plt.bar(df.index, df['T'], color='c', label=lv, align='center')
    plt.legend(loc='lower left')

    ax2 = ax1.twinx()
    ax2.set_xticklabels(x, rotation=90, size="small")
    for i, j in enumerate(PairLabel):
        lv = j + ':' + "{:,}".format(df.iloc[-1][j])
        plt.plot(df.index, df[j], PairColor[i], label=lv)
        t.append(lv)
    plt.legend(loc='upper left')

    ti = ' '.join(t)
    tb = "{:,}".format(df.iloc[-1]['T'])
    title = 'T:{x} ({y})'.format(x=tb, y=ti)
    plt.title(title)
    plt.savefig(PngFile)
    plt.show()


data = ReadCsv(CsvFile)
df = data.getData()
ax = data.getIndex()
myPlot(df, ax)
