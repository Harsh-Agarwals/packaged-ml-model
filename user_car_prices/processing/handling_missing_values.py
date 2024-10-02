import numpy as np
from sklearn.impute import KNNImputer
from user_car_prices.config import config
from sklearn.base import BaseEstimator, TransformerMixin
imputer = KNNImputer(n_neighbors=5, weights='distance')

class MissingValueImputation(BaseEstimator, TransformerMixin):
    def __init__(self, imputer_columns):
        self.imputer_columns = imputer_columns

    def fit(self, X, y=None):
        self.imputed_cols = imputer.fit_transform(X[self.imputer_columns])
        return self
    
    def tranform(self, X, y=None):
        X['clean_title'].fillna('No', inplace=True)
        X['accident'].bfill(inplace=True)
        X.loc[X['fuel_type'] == '–', 'fuel_type'] = np.nan
        X['fuel_type'].fillna('Gasoline', inplace=True)
        X[self.imputer_columns] = self.imputed_cols
        return X

class NewFeaturesMissingImputation(BaseEstimator, TransformerMixin):
    def __init__(self, new_features):
        self.new_features = new_features

    def fit(self, X, y=None):
        self.imputed_features = imputer.fit_transform(X[self.new_features])
        return self
    
    def transform(self, X, y=None):
        X[self.new_features] = self.imputed_features
        return X
    
# def train_missing_value_imputation(df):
#     df['clean_title'].fillna('No', inplace=True)
#     df['accident'].bfill(inplace=True)
#     df.loc[df['fuel_type'] == '–', 'fuel_type'] = np.nan
#     df['fuel_type'].fillna('Gasoline', inplace=True)    
#     imputed_df = imputer.fit_transform(df[['milage', 'price']])
#     df[['milage', 'price']] = imputed_df
#     return df

# def predict_missing_value_imputation(df):
#     df['clean_title'].fillna('No', inplace=True)
#     df['accident'].bill(inplace=True)
#     df.loc[df['fuel_type'] == '–', 'fuel_type'] = np.nan
#     df['fuel_type'].fillna('Gasoline', inplace=True)
#     imputed_df = imputer.fit_transform(df[['milage']])
#     df[['milage']] = imputed_df
#     return df

# def new_features_missing_imputation(df):
#     imputed_df = imputer.fit_transform(df[config.NEW_FEATURES])
#     df[config.NEW_FEATURES] = imputed_df
#     return df