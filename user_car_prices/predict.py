import os
import sys
import random
import numpy as np
import pandas as pd
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs'))
from logging_file import logger

# This makes sure our package is found
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import warnings
warnings.filterwarnings('ignore')

from user_car_prices.config import config
from user_car_prices.processing import data_handling

model_pipeline = data_handling.load_pipeline()

def create_predictions(df):
    data = pd.DataFrame(df)
    # logger.info(data)
    print(data)
    if data.T.shape[0]==1:
        rows = get_train_rows()
        data = pd.concat([rows, data.T], axis=0, ignore_index=True)
        data.reset_index(drop=True, inplace=True)
        preds = model_pipeline.predict(data[config.MODEL_FEATURES])
        preds = preds[3]
    elif data.shape[0]==1:
        rows = get_train_rows()
        data = pd.concat([rows, data], axis=0, ignore_index=True)
        data.reset_index(drop=True, inplace=True)
        preds = model_pipeline.predict(data[config.MODEL_FEATURES])
        preds = preds[3]
    else:
        preds = model_pipeline.predict(data[config.MODEL_FEATURES])
    print(f"Predictions: {preds}")
    return preds

def generate_predictions():
    test = data_handling.load_dataset(config.TEST_FILE)
    predictions = model_pipeline.predict(test[config.MODEL_FEATURES])
    print(predictions)
    # logger.info("\nPredictions")
    # logger.info(predictions)
    return predictions

def get_train_rows():
    test = data_handling.load_dataset(config.TRAIN_FILE)
    n = test.shape[0]
    indexes = random.sample(range(n), 3)
    df = test.iloc[indexes, :]
    # logger.warning("\nTraining Rows:")
    # logger.warning(df)
    return df

def get_few_rows():
    test = data_handling.load_dataset(config.TEST_FILE)
    n = test.shape[0]
    indexes = random.sample(range(n), 3)
    df = test.iloc[indexes, :]
    # logger.warning("\nFew Rows:")
    # logger.warning(df)
    return df

def get_one_row():
    test = data_handling.load_dataset(config.TEST_FILE)
    n = test.shape[0]
    index = random.choice(range(n))
    df = test.iloc[index, :]
    # logger.warning("\nOne Row:")
    # logger.warning(df)
    return pd.DataFrame(df)

if __name__=="__main__":
    # Test set predictions
    generate_predictions()

    # Predicting few rows
    # rows = get_few_rows()
    # create_predictions(rows)

    # Predicting one row
    # row = get_one_row()
    # create_predictions(row)
