import pytest

import os
import sys
from pathlib import Path

# This makes sure our package is found
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import warnings
warnings.filterwarnings('ignore')

from user_car_prices.config import config
from user_car_prices.processing.data_handling import load_dataset
from user_car_prices.predict import create_predictions, get_one_row

@pytest.fixture
def script_testing():
    row = get_one_row()
    result = create_predictions(row)
    return result

# Checking result in not Null
def test_output_is_not_null(script_testing):
    assert script_testing[0] is not None

# Checking result is floating type
def test_output_is_floating_type(script_testing):
    assert isinstance(script_testing[0], float)
