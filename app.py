
# Smart Delivery Slot Predictor (Basic Project for CSE Freshers)
# Flask API with Decision Tree Classifier

from flask import Flask, request, jsonify, render_template
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import random
import os

app = Flask(__name__)

# Simulated training data
# Features: [order_hour (0-23), current_load (0-100), area_type (0 = urban, 1 = suburban)]
# Target: [0 = Not available, 1 = Available]
X = []
y = []

# Generate sample training data
for _ in range(300):
    hour = random.randint(0, 23)
    load = random.randint(0, 100)
    area = random.randint(0, 1)
    available = 1 if (load < 70 and (hour >= 9 and hour <= 21)) else 0
    X.append([hour, load, area])
    y.append(available)

model = DecisionTreeClassifier()
model.fit(X, y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    order_hour = int(request.form.get('order_hour'))
    current_load = int(request.form.get('current_load'))
    area_type = int(request.form.get('area_type'))

    features = [[order_hour, current_load, area_type]]
    prediction = model.predict(features)
    result = "Available" if prediction[0] == 1 else "Not Available"
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
