import pandas as pd

class ReadCsv:
    def __init__(self, csvfile, index_col):
        self.data = pd.read_csv(csvfile, index_col=0)

    def getData(self):
        data['Total'] = data.sum(axis=1)
        return data

    def getIndex(self):
        
