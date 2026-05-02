# 📈 AI-Powered Demand Forecasting

A machine learning web application that predicts product sales demand based on store, item, promotional, and temporal features.

🔗 **Live App:** [https://ai-powered-demand-forecasting.streamlit.app](https://ai-powered-demand-forecasting.streamlit.app)

---

## 🚀 Features

- **Single Prediction** — Enter store/item details and get instant sales forecast
- **Batch Prediction** — Upload a CSV file and download results with predicted sales
- **Interactive Chart** — Visual comparison of lag features vs predicted sales
- **Region Support** — North, South, East, West one-hot encoding
- **Auto Model Download** — Model loads from Google Drive on first run

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Scikit-learn | ML model (Random Forest / Gradient Boosting) |
| Streamlit | Web app framework |
| Pandas | Data processing |
| gdown | Google Drive model download |

---

## 📊 Input Features

| Feature | Description |
|---------|-------------|
| Store ID | Unique store identifier |
| Item ID | Unique product identifier |
| Promotion | Whether promotion is active (0/1) |
| Holiday | Whether it's a holiday (0/1) |
| Temperature | Current temperature |
| Fuel Price | Current fuel price |
| Month | Month of the year (1-12) |
| Day | Day of the month (1-31) |
| Day of Week | 0 = Monday, 6 = Sunday |
| Week of Year | Week number (1-52) |
| Lag_1 | Yesterday's sales |
| Lag_7 | Sales from 7 days ago |
| Rolling Mean 7 | 7-day average sales |
| Region | North / South / East / West |

---

## 📂 Project Structure

```
AI-Powered-Demand-Forecasting/
├── app.py                            # Streamlit web app
├── requirements.txt                  # Python dependencies
├── forecast_columns.pkl              # Feature column names
├── demand_forecasting.csv            # Training dataset
└── ai_powered_demand_forecasting.ipynb  # Model training notebook
```

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Ojas4git/AI-Powered-Demand-Forecasting.git
cd AI-Powered-Demand-Forecasting

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your model file
# Place model_forecast.pkl in the project folder

# 4. Run the app
streamlit run app.py
```

---

## 🌐 Deployment

This app is deployed on **Streamlit Cloud**.
The ML model (`model_forecast.pkl`) is hosted on Google Drive and downloaded automatically at runtime using `gdown`.

---

## 📸 Screenshot

![App Screenshot](https://i.imgur.com/placeholder.png)
> *Replace this with an actual screenshot of your app*

---

## 👤 Author

**Ojas** — [GitHub](https://github.com/Ojas4git)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
