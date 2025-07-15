import pandas as pd
from xgboost import XGBRegressor
import joblib

# Load your dataset
df = pd.read_csv("nba_salaries_2.csv")  # Replace with actual file path

# Define features and target
features = ['Age', 'PTS', 'GP', 'FT%']
X = df[features]
y = df["Salary"]

# Train model
model = XGBRegressor()
model.fit(X, y)

# Save the model to disk
joblib.dump(model, "salary_predictor_model.pkl")
print("Model saved as salary_predictor_model.pkl")