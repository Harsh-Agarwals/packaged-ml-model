import os
import joblib
import pandas as pd
from user_car_prices.config import config

def load_dataset(DATASET):
    file_path = os.path.join(config.DATAPATH, DATASET)
    data = pd.read_csv(file_path)
    return data

def save_pipeline(pipeline_to_save):
    model_path = os.path.join(config.MODEL_SAVED_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, model_path)
    print(f"{pipeline_to_save} saved to {model_path}!")

def load_pipeline():
    model_path = os.path.join(config.MODEL_SAVED_PATH, config.MODEL_NAME)
    model = joblib.load(model_path)
    print(f"{config.MODEL_NAME} loaded from {model_path}!")
    return model