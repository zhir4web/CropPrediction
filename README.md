# Crop Prediction Dashboard

An intelligent agricultural analytics application that uses Machine Learning to recommend the most suitable crops based on soil and weather conditions.

## 📋 Overview

This project is a web-based decision support system for farmers and agricultural experts. It leverages a Random Forest Classifier to analyze environmental parameters (Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall) and predict the optimal crop for cultivation. The system aims to maximize crop yield by recommending plants best suited to specific environmental contexts.

## ✨ Features

- **Precise Crop Prediction**: Uses a trained Machine Learning model to recommend crops with high accuracy.
- **Interactive Dashboard**: A modern, responsive web interface for easy data entry and visualization.
- **Real-time Analytics**:
    - **Soil Analysis**: Comparison of your soil's nutrient levels (N, P, K) against optimal standards.
    - **Weather Insights**: Analysis of temperature, humidity, and rainfall conditions.
- **Visualizations**: Interactive charts (Bar and Radar) powered by Chart.js to visualize soil composition.
- **Data Statistics**: Overview of the training dataset, including total samples and averages.

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Chart.js)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Processing**: Pandas, NumPy
- **Serialization**: Pickle

## 📂 Project Structure

```
Crop-Prediction-app/
├── app.py                  # Main Flask application file
├── model.py                # Script to train and save the ML model
├── model.pkl               # Trained serialized model
├── requirements.txt        # List of Python dependencies
├── Dataset/
│   └── Crop_recommendation.csv  # Dataset used for training
├── static/
│   └── style.css           # Custom CSS styles
└── templates/
    └── index.html          # Main dashboard HTML template
```

## 🚀 Installation & Setup

1.  **Clone the Repository** (if applicable) or download the source code.

2.  **Install Dependencies**
    Ensure you have Python installed. Run the following command to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Train the Model (Optional)**
    The project comes with a pre-trained `model.pkl`. If you wish to retrain it:
    ```bash
    python model.py
    ```

4.  **Run the Application**
    Start the Flask server:
    ```bash
    python app.py
    ```

5.  **Access the Dashboard**
    Open your web browser and go to:
    `http://127.0.0.1:5000/`

## 📊 How to Use

1.  **Enter Data**: Fill in the form on the dashboard with your soil and weather data (N, P, K, Temp, Humidity, pH, Rainfall).
2.  **Predict**: Click the "Analyze & Predict" button.
3.  **View Results**:
    - The recommended crop will appear on the card.
    - The "Soil Composition Trends" chart will update to compare your input with average optimal levels.
    - The "Soil Analytics" and "Weather Insights" sections will provide detailed feedback on your environmental conditions.

## 💾 Dataset

The model is trained on the `Crop_recommendation.csv` dataset, which contains records of soil and weather conditions for various crops.

## 👥 Credits

Developed by:
- Ahmad Yasin
- Dawan Star
- Pairaw Kamil
- Zhir Jalal
