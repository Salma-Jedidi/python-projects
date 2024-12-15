from flask import Flask, render_template, request, jsonify, redirect
import numpy as np
import pickle
import pandas as pd


# Initialisation de l'application Flask
app = Flask(__name__)

# Chargement du modèle
model_path = "models/model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Route principale (affichage du formulaire HTML)
@app.route("/")
def index():
    return render_template("index.html")

# Route pour la prédiction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract features from JSON
        input_data = [
            float(data["sqft_living"]),
            float(data["bedrooms"]),
            float(data["bathrooms"]),
            float(data["sqft_above"]),
            float(data["sqft_living15"]),
            float(data["grade"])
        ]

        # Convert to DataFrame
        df = pd.DataFrame([input_data], columns=["sqft_living", "bedrooms", "bathrooms", "sqft_above", "sqft_living15", "grade"])

        # Make prediction
        prediction = model.predict(df)[0]

        # Return prediction as a response
        return jsonify({"prediction_text": f"Estimated Price: ${prediction:,.2f}"})
    except Exception as e:
        return jsonify({"error": str(e)})


# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)
