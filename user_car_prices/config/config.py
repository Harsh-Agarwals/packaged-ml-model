import os
import pathlib
import user_car_prices

PACKAGE_ROOT = pathlib.Path(user_car_prices.__file__).resolve().parent
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

MODEL_NAME = "model.pkl"
MODEL_SAVED_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = "price"
MODEL_FEATURES = ['brand', 'model', 'model_year', 'milage', 'fuel_type', 'engine', 'transmission', 'ext_col', 'int_col', 'accident', 'clean_title']

FEATURES_WITH_OUTLIERS = ['milage']
OUTLIER_RANGE = [[5000, 500000]]

NEW_FEATURES = ['HP', 'litres']

FEATURE_TO_ENCODE = ['accident', 'clean_title', 'ext_col', 'int_col', 'transmission', 'fuel_type', 'engine']

FEATURES_TO_DROP = ['brand', 'model']

FEATURES_TO_SCALE = ['model_year', 'milage', 'engine', 'transmission',
       'ext_col', 'int_col', 'HP', 'litres', 'brand', 'model']