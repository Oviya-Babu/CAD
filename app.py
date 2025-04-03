
from flask import Flask, request, render_template, jsonify
import joblib

import os

app = Flask(__name__)



model_filepath = os.path.join(os.getcwd(), "phishing_email_model.pkl")
model = joblib.load(model_filepath)

@app.route("/", methods=["GET", "POST"])
def home():
    """Renders the homepage and handles form submission for email classification."""
    prediction_result = None

    if request.method == "POST":
        email_text = request.form.get("email_text", "").strip()
        
        if email_text:
            

            phishing_probability = model.predict_proba([email_text])[0][1]
            threshold = 0.4  

            prediction_result = "Phishing" if phishing_probability > threshold else "Not Phishing"

    return render_template("index.html", prediction=prediction_result)

@app.route("/detect", methods=["POST"])

def detect_phishing():
    """API endpoint for phishing detection using JSON requests."""
    try:
        request_data = request.get_json()
        print("Received request data:", request_data)  

        email_text = request_data.get("email_text", "").strip()
        if not email_text:
            return jsonify({"error": "Email text is required"}), 400

        # Predict probability and classify
        phishing_probability = model.predict_proba([email_text])[0][1]
        threshold = 0.4  

        classification = "Phishing" if phishing_probability > threshold else "Not Phishing"


        return jsonify({"result": classification, "confidence": phishing_probability})

    except Exception as error:

        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True)
