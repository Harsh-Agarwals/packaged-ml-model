import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class AddNewFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['HP'] = X.engine.apply(lambda x: x[:x.index('H')] if 'H' in x else np.nan)
        X['litres'] = X.engine.apply(lambda x: ''.join(list(filter(lambda x: x.count('L')==1, x.split(' '))))[:-1])

        X['HP'] = pd.to_numeric(X['HP'], errors='coerce')
        X['litres'] = pd.to_numeric(X['litres'], errors='coerce')
        print("New features added!")
        return X


# def adding_new_features(df):
#     df['HP'] = df.engine.apply(lambda x: x[:x.index('H')] if 'H' in x else np.nan)
#     df['litres'] = df.engine.apply(lambda x: ''.join(list(filter(lambda x: x.count('L')==1, x.split(' '))))[:-1])

#     df['HP'] = pd.to_numeric(df['HP'], errors='coerce')
#     df['litres'] = pd.to_numeric(df['litres'], errors='coerce')

#     return df