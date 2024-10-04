import numpy as np
from user_car_prices.config import config
from sklearn.base import BaseEstimator, TransformerMixin

class OutlierRemoval(BaseEstimator, TransformerMixin):
    def __init__(self, outlier_variables, variable_range):
        self.outlier_variables = outlier_variables
        self.variable_range = variable_range
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        for i, variable in enumerate(self.outlier_variables):
            if variable in X.columns:
                X.loc[(X[variable] <= self.variable_range[i][0]) | (X[variable] >= self.variable_range[i][1]), variable] = np.nan
        print("Outlier removed!")
        return X

# def remove_outlier(df):
#     for i, column in enumerate(config.FEATURES_WITH_OUTLIERS):
#         if column in df.columns:
#             df.loc[(df[column] <= config.OUTLIER_RANGE[i][0]) | (df[column] >= config.OUTLIER_RANGE[i][1]), column] = np.nan
#         else:
#             pass
#     return df