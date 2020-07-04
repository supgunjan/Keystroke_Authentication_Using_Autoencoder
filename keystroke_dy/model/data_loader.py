import pandas as pd
import numpy

class loader:

    def __init__(self):
        data = pd.read_csv('./Rekita.csv', header=None)
        X = data.iloc[:, 2:]
        self.w = len(data.iloc[0, 1])
        self.train_x = X.to_numpy()

    def load(self):
        return self.train_x, self.train_x, self.w