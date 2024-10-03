import os
from user_car_prices.config import config

with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as f:
    config.__version__ = f.read().strip()