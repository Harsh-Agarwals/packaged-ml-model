import os
from pathlib import Path
import sys

# This makes sure our package is found
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import user_car_prices
try:
    print(user_car_prices.__version__)
except Exception as e:
    print(f"Error: {e}")