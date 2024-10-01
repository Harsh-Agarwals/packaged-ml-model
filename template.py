import os
import logging
from datetime import datetime
from pathlib import Path

today = datetime.now()
logging_path = os.path.join(os.path.dirname("."), "logs")

if os.path.exists(logging_path):
    print("Logging path exists")
    logging.basicConfig(filename=os.path.join(logging_path, f"log_{today.strftime("%d%m%Y")}.log"), filemode='w', format='%(message)s', force=True)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.warning("==============LOGGER START==============")
    logger.info(f"Current time: {today}")
    logger.warning("-----------------------------\n\n")
else:
    os.makedirs("logs")
    logging.basicConfig(filename=os.path.join(logging_path, f"log_{today.strftime("%d%m%Y")}.log"), filemode='w', format='%(message)s', force=True)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.warning("==============LOGGER START==============")
    logger.info(f"Current time: {today}")
    logger.warning("-----------------------------\n\n")

project_path = "user_car_prices"

files = [
    f"{project_path}/__init__.py",
    f"{project_path}/config/__init__.py",
    f"{project_path}/config/config.py",
    f"{project_path}/datasets/__init__.py",
    f"{project_path}/processing/__init__.py",
    f"{project_path}/research/trails.ipynb",
    f"{project_path}/trained_models/__init__.py",
    f"{project_path}/utils/__init__.py",
    f"{project_path}/utils/evaluation.py",
    f"{project_path}/pipeline.py",
    f"{project_path}/predict.py",
    f"{project_path}/training_pipeline.py",
    "static/style.css",
    "templates/dashboard.html",
    "templates/index.html",
    "tests/pytest.ini",
    "tests/test_prediction.py",
    "manifest.in",
    "setup.py",
    "app.py",
    "model_script.ipynb"
]

for file in files:
    directory = os.path.dirname(file)
    filename = os.path.basename(file)

    if directory != "":
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.warning(f"\nNew directory {directory} inserted")

    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write('')
            logger.warning(f"New file {file} inserted")
        
