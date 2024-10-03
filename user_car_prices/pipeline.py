import os
from sklearn.pipeline import Pipeline
from user_car_prices.processing import outlier_handling as oh
from user_car_prices.processing import handling_missing_values as hmv
from user_car_prices.processing import feature_engineering as fe
from user_car_prices.processing import preprocessing as pp
from user_car_prices.config import config
from sklearn.ensemble import GradientBoostingRegressor

model_pipeline = Pipeline([
    ('Outlier Detection', oh.OutlierRemoval(outlier_variables=config.FEATURES_WITH_OUTLIERS, variable_range=config.OUTLIER_RANGE)),
    ('Missing Value Imputation', hmv.MissingValueImputation(imputer_columns=config.FEATURES_WITH_OUTLIERS)),
    ('Adding new feature', fe.AddNewFeatures()),
    ('New Features missing imputation', hmv.NewFeaturesMissingImputation(new_features=config.NEW_FEATURES)),
    ('Encoding features', pp.EncodingFeatures(features_to_encode=config.FEATURE_TO_ENCODE, features_to_drop=config.FEATURES_TO_DROP)),
    ('Scaling features', pp.ScalingFeatures(features_to_scale=config.FEATURES_TO_SCALE)),
    ('Gradient Boosting Regressor', GradientBoostingRegressor())
])