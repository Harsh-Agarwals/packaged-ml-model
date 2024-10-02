import os
import pathlib
import user_car_prices

PACKAGE_ROOT = pathlib.Path(user_car_prices.__path__).resolve().parent
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

MODEL_NAME = "model.pkl"
MODEL_SAVED_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = "price"
MODEL_FEATURES = ['brand', 'model', 'model_year', 'milage', 'fuel_type', 'engine', 'transmission', 'ext_col', 'internal_col', 'accident', 'clean_title']

FEATURES_WITH_OUTLIERS = ['milage', 'price']
OUTLIER_RANGE = [[5000, 500000], [2500, 250000]]

FEATURES_TO_FILLNA = ['clean_title', 'accident', 'fuel_type']

NEW_FEATURES = ['HP', 'litres']

FEATURE_TO_ENCODE = ['accident', 'clean_title', 'ext_col', 'int_col', 'transmission', 'fuel_type', 'engine']

FEATURES_TO_DROP = ['id', 'brand', 'model']

FEATURES_TO_SCALE = ['model_year', 'milage', 'engine', 'transmission',
       'ext_col', 'int_col', 'HP', 'litres', 'brand', 'model']