import os
from setuptools import find_packages, setup
from pathlib import Path

import warnings
warnings.filterwarnings('ignore')

# Metadata
NAME='car-prices-model'
DESCRIPTION='ML model package for prediction of Car Prices'
URL='https://github.com/Harsh-Agarwals/MLops/tree/main/Packaging-ML-Model'
EMAIL='harshag.code@gmail.com'
AUTHOR='Harsh Agarwal'
REQUIRES_PYTHON='>=3.7.0'

pwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(pwd, "requirements.txt")) as reqm:
    requirements = reqm.readlines()

requirements = [req.strip() for req in requirements]

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'user_car_prices'
about = {}

with open(PACKAGE_DIR / 'VERSION') as version:
    vx = version.read().strip()
    about['__version__'] = vx

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model': ['VERSION']},
    install_requires=requirements,
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)