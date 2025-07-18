# 🏀 NBA Salary Predictor

This project is a machine learning web application that predicts the **salary of NBA players** based on performance statistics.

🔮 Built using:
- **Python + Flask** for backend API
- **Scikit-learn + XGBoost** for model training
- **Render** for backend deployment
- **GitHub Pages + HTML/JavaScript** for frontend

---

## Live Demo

- **Frontend:** [GitHub Pages](https://ripslinger77.github.io/nba-salary-predictor/)
- **Backend API:** [Render URL](https://nba-salary-predictor.onrender.com)

---

## Features Used for Prediction

The trained model uses **4 key features**:
- `Age`
- `PTS` (Points Per Game)
- `GP` (Games Played)
- `FT%` (Free Throw Percentage)

These features were selected using **forward feature selection** to minimize model error.

---

## Model Training

The model was trained using **XGBoost Regressor** on a dataset of 500 NBA players. Feature engineering and evaluation were done in Jupyter notebooks inside the `archive/` folder.

> Final model RMSE: ~4.64M — considering salary range ($1M to $50M), this is acceptable for estimation purposes.

---

## Project Structure

```
nba-salary-predictor/
│
├── archive/                 # Jupyter notebooks (exploration, modeling)
├── data/                    # Raw NBA salary/stat data
├── models/                  # Saved XGBoost model (joblib)
├── scripts/                 # Helper scripts for model loading/prediction
│
├── salary-predictor-api/   # Flask backend
│   ├── app.py               # API routes
│   └── requirements.txt     # Python dependencies
│
├── frontend/                # HTML + JavaScript frontend
│   ├── index.html
│   └── script.js
```

---

## Local Development

### Backend

```bash
cd salary-predictor-api
pip install -r requirements.txt
python app.py
```

### Frontend

Just open `frontend/index.html` in your browser. Update the API endpoint in `script.js` if needed.

---

## Deployment

- **Backend** hosted on [Render](https://render.com/)
  - Flask API loads the `.pkl` model and returns salary prediction.
  - Kept warm using [UptimeRobot](https://uptimerobot.com/).
- **Frontend** hosted via GitHub Pages

---

## API Usage

`POST /predict` — Predicts salary

**Request JSON:**
```json
{
  "Age": 28,
  "PTS": 24.5,
  "GP": 72,
  "FT%": 85.3
}
```

**Response:**
```json
{
  "predicted_salary": 23782011.73
}
```

---

## Future Work

- Improve frontend
- Research and improve feature selection methodology.
- Improve model with more features (collect more data) and try other ML algorithms
- Maintain DB of historical salaries of players and predictions made by the model for comparison

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- NBA data sourced from [kaggle.com](https://www.kaggle.com/datasets/jamiewelsh2/nba-player-salaries-2022-23-season)
- Deployment via Render and GitHub Pages
