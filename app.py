import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

# Load dataset for statistics
df = pd.read_csv('Dataset/Crop_recommendation.csv')

def get_stats(input_data=None):
    stats = {
        'total_samples': len(df),
        'unique_crops': df['label'].nunique(),
        'avg_n': round(df['N'].mean(), 1),
        'avg_p': round(df['P'].mean(), 1),
        'avg_k': round(df['K'].mean(), 1),
        'avg_temp': round(df['temperature'].mean(), 1),
        'avg_hum': round(df['humidity'].mean(), 1),
        'avg_ph': round(df['ph'].mean(), 1),
        'avg_rain': round(df['rainfall'].mean(), 1),
        'current': input_data
    }
    
    return stats

@flask_app.route("/")
def Home():
    stats = get_stats()
    return render_template("index.html", stats=stats)

@flask_app.route("/predict", methods = ["POST"])
def predict():
    # Explicitly get features to ensure order
    input_data = {
        'N': float(request.form.get('Nitrogen', 0)),
        'P': float(request.form.get('Phosphorus', 0)),
        'K': float(request.form.get('Potassium', 0)),
        'temp': float(request.form.get('temperature', 0)),
        'hum': float(request.form.get('humidity', 0)),
        'ph': float(request.form.get('pH', 0)),
        'rain': float(request.form.get('rainfall', 0))
    }
    
    features = [np.array([input_data['N'], input_data['P'], input_data['K'], 
                         input_data['temp'], input_data['hum'], input_data['ph'], 
                         input_data['rain']])]
    
    prediction = model.predict(features)
    stats = get_stats(input_data)
    
    return render_template("index.html", 
                         prediction_text="The Predicted Crop is {}".format(prediction[0]), 
                         stats=stats,
                         prediction=prediction[0])

if __name__ == "__main__":
    flask_app.run(debug=True)
