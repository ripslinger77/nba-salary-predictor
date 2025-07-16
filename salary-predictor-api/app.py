from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model at startup
model = joblib.load("models\salary_predictor_model.pkl")

@app.route("/predict", methods=["POST"])
def predict_salary():
    try:
        data = request.get_json()

        # Extract features
        age = float(data.get("Age"))
        pts = float(data.get("PTS"))
        gp = float(data.get("GP"))
        ft_percent = float(data.get("FT%"))

        # Prepare input
        input_array = np.array([[age, pts, gp, ft_percent]])

        # Make prediction
        salary = float(model.predict(input_array)[0])

        return jsonify({"predicted_salary": round(salary, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def index():
    return "NBA Salary Predictor API is running!"

if __name__ == "__main__":
    app.run(debug=True)