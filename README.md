# 📈 AI-Powered Demand Forecasting System

🔗 **Live Application:** https://ai-powered-demand-forecasting.streamlit.app

---

## 📌 Project Overview

This project presents an **end-to-end Machine Learning system** designed to predict product demand across retail stores using historical sales data, temporal features, and external factors.

The application enables businesses to **forecast future demand**, optimize inventory planning, and reduce operational inefficiencies.

---

## 🎯 Business Problem

Accurate demand forecasting is critical for:

* Preventing **stockouts and overstocking**
* Improving **inventory and supply chain efficiency**
* Reducing **operational costs**
* Enhancing **customer satisfaction**

This project aims to provide **data-driven demand predictions** using machine learning.

---

## ⚙️ Tech Stack

| Tool          | Purpose                    |
| ------------- | -------------------------- |
| Python        | Core programming language  |
| Pandas, NumPy | Data processing            |
| Scikit-learn  | Machine learning models    |
| Streamlit     | Web application deployment |
| gdown         | Model hosting & retrieval  |
| Git & GitHub  | Version control            |

---

## 📊 Input Features

The model uses a combination of **categorical, numerical, and time-series features**:

* Store_ID, Item_ID
* Promotion, Holiday
* Temperature, Fuel Price
* Month, Day, Day_of_Week, Week_of_Year
* Lag_1 (Previous day sales)
* Lag_7 (Previous week sales)
* Rolling_Mean_7 (7-day average demand)
* Region (One-hot encoded)

---

## 🧠 Machine Learning Approach

### 1. Data Preprocessing

* Converted date features into time-based variables
* Applied **binary encoding** for Promotion & Holiday
* Used **one-hot encoding** for Region
* Ensured consistent feature alignment for model training

---

### 2. Feature Engineering (Key Highlight)

To capture temporal patterns, the following features were engineered:

* **Lag Features:**

  * Lag_1 → Previous day demand
  * Lag_7 → Weekly pattern

* **Rolling Features:**

  * 7-day moving average

These features are critical for **time-series forecasting in real-world systems**.

---

### 3. Model Development

Models implemented:

* **Random Forest (Selected Model)**
* **XGBoost (Benchmark Model)**

👉 Random Forest was selected based on better performance on evaluation metrics.

---

### 4. Model Evaluation

Metrics used:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

> Insight: Model performance was limited due to synthetic dataset characteristics, highlighting the importance of data quality in forecasting tasks.

---

## 🚀 Deployment

The model is deployed using **Streamlit Cloud** with the following capabilities:

* 🔮 Real-time demand prediction
* 📂 Batch prediction via CSV upload
* 📊 Interactive visualization of inputs vs predictions
* ☁️ Automatic model download from Google Drive

---

## 💻 How to Run Locally

```bash
# Clone repository
git clone https://github.com/Ojas4git/AI-Powered-Demand-Forecasting.git
cd AI-Powered-Demand-Forecasting

# Install dependencies
pip install -r requirements.txt

# Add model file manually (for local run)
# Place model_forecast.pkl in project folder

# Run application
streamlit run app.py
```

---

## 📂 Project Structure

```bash
AI-Powered-Demand-Forecasting/
│
├── app.py                              # Streamlit application
├── requirements.txt                    # Dependencies
├── forecast_columns.pkl                # Feature schema
├── demand_forecasting.csv              # Dataset
├── ai_powered_demand_forecasting.ipynb # Model training notebook
```

---

## 🔥 Key Highlights

* End-to-end ML pipeline (EDA → Feature Engineering → Modeling → Deployment)
* Implementation of **time-series feature engineering (lag & rolling features)**
* Model comparison and selection (Random Forest vs XGBoost)
* Fully deployed interactive application
* Solved real-world deployment challenges (large model hosting)

---

## 📈 Future Improvements

* Incorporate real-world datasets with stronger temporal patterns
* Implement advanced models (LSTM, Prophet)
* Add real-time data integration
* Improve forecasting accuracy with hyperparameter tuning

---

n-source and available under the MIT License.
