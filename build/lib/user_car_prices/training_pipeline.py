import os
from pathlib import Path
import sys

# This makes sure our package is found
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from user_car_prices.processing import data_handling
from user_car_prices.config import config
from user_car_prices import pipeline

def perform_training():
    train_data = data_handling.load_dataset(config.TRAIN_FILE)
    target = train_data[config.TARGET]
    pipeline.model_pipeline.fit(train_data[config.MODEL_FEATURES], target)
    data_handling.save_pipeline(pipeline_to_save=pipeline.model_pipeline)

if __name__=="__main__":
    perform_training()