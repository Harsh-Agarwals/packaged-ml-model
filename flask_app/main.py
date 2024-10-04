from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import sys
from pathlib import Path
import os

# This makes sure our package is found
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from user_car_prices.predict import create_predictions

app = Flask(__name__)

@app.route('/car-prices-prediction', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.to_dict()
        for col in ['accident', 'clean_title']:
            if col not in data.keys():
                data[col] = ''
        data = pd.DataFrame(data, index=[0])
        data['model_year'] = data['model_year'].astype('int32')
        data['milage'] = data['milage'].astype('int32')
        prediction = create_predictions(data)
        return redirect(url_for('dashboard', prediction=f"{prediction[3]:.2f}"))
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    prediction = request.args.get('prediction')
    return render_template("dashboard.html", prediction=prediction)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)