import streamlit as st
import pandas as pd
import sys
from pathlib import Path
import os

# This makes sure our package is found
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from user_car_prices.predict import create_predictions

st.title("Car Prices predictions")
st.text("Fill in the required properties to get the predicted Car Prices.")

brand = st.text_input("Brand", placeholder="Brand")
model = st.text_input("Model", placeholder="Model")
model_year = st.number_input("Model Year", placeholder="Model Year")
milage = st.number_input("Mileage", placeholder="Milage")
fuel_type = st.selectbox("Fuel Type", ("Gasoline", "Hybrid", "E85 Flex Fuel", "Diesel", "Plug-In Hybrid", "not supported"), placeholder="Fuel Type")
engine = st.text_input("Engine", placeholder="Engine")
transmission = st.text_input("Transmission", placeholder="Transmission")
ext_col = st.text_input("External Color", placeholder="External Color")
int_col = st.text_input("Internal Color", placeholder="Internal Color")
accident = st.radio("Accident", options=["None reported", "At least 1 accident or damage reported"])
clean_title = st.radio("Clean Title", options=["Yes", "No"])

if st.button('Predict'):
    data = {'brand': brand, 'model': model, 'model_year': model_year, 'milage': milage, 'fuel_type': fuel_type, 'engine': engine, 'transmission': transmission, 'ext_col': ext_col, 'int_col': int_col, 'accident': accident if accident else '', 'clean_title': clean_title if clean_title else ''}
    data = pd.DataFrame(data, index=[0])
    prediction = create_predictions(data)
    prediction = f"{prediction:.2f}"
    st.title(f"Prediction: {prediction}")