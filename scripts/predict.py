import joblib
import numpy as np

model = joblib.load("salary_predictor_model.pkl")

# Input: [Age, PTS, GP, FT%]
player_input = [24, 22.4, 75, 0.87]

# Ensure input is 2D array (n_samples, n_features)
input_array = np.array(player_input).reshape(1, -1)

predicted_salary = model.predict(input_array)[0]

print(f"Predicted Salary: ${predicted_salary:,.2f}")