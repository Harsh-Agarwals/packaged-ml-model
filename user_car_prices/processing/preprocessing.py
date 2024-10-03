from user_car_prices.config import config
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

le = LabelEncoder()
ss = StandardScaler()

model_encoders = {}

def encoding_product(row, df):
    brand = row['brand']
    model = row['model']
    if brand not in model_encoders:
        model_encoders[brand] = LabelEncoder()
        model_encoders[brand].fit(df[df['brand']==brand]['model'])
    return model_encoders[brand].transform([model])[0]

class EncodingFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_encode, features_to_drop):
        self.features_to_encode = features_to_encode
        self.features_to_drop = features_to_drop

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['brand_encoded'] = le.fit_transform(X['brand'])
        X['model_encoded'] = X.apply(lambda row: encoding_product(row, X), axis=1)

        for feature in self.features_to_encode:
            X[feature] = le.fit_transform(X[feature])

        print(X.columns)
        X.drop(columns=self.features_to_drop, inplace=True)
        X.rename(columns={'brand_encoded': 'brand', 'model_encoded': 'model'}, inplace=True)
        print("Features encoded!")
        print(X.columns)
        return X

class ScalingFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_scale):
        self.features_to_scale = features_to_scale

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X[self.features_to_scale] = ss.fit_transform(X[self.features_to_scale])
        print("Feature scaled!")
        return X
    
# def encoding_features(df):
#     df['brand_encoded'] = le.fit_transform(df['brand'])
#     df['model_encoded'] = df.apply(lambda row: encoding_product(row, df), axis=1)

#     for column in config.FEATURE_TO_ENCODE:
#         df[column] = le.fit_transform(df[column])
#     df.drop(columns=config.FEATURES_TO_DROP, inplace=True)
#     df.rename(columns={'brand_encoded': 'brand', 'model_encoded': 'model'}, inplace=True)

#     return df

# def scaling_features(df):
#     df[config.FEATURES_TO_SCALE] = ss.fit_transform(df[config.FEATURES_TO_SCALE])
#     return df

