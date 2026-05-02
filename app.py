import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Demand Forecasting", layout="wide")

# Load model and columns

model = pickle.load(open('model_forecast.pkl', 'rb'))
columns = pickle.load(open('forecast_columns.pkl', 'rb'))

st.title("📈 AI-Powered Demand Forecasting")
st.markdown("---")

# ------------------- INPUT SECTION -------------------

st.subheader("Enter Input Features")

col1, col2 = st.columns(2)

with col1:
store = st.number_input("Store ID", value=1)
item = st.number_input("Item ID", value=101)
promotion = st.selectbox("Promotion", [0,1])
holiday = st.selectbox("Holiday", [0,1])
temp = st.number_input("Temperature", value=30)
fuel = st.number_input("Fuel Price", value=3.5)

with col2:
month = st.slider("Month", 1, 12, 1)
day = st.slider("Day", 1, 31, 1)
dow = st.slider("Day of Week (0=Mon)", 0, 6, 1)
week = st.slider("Week of Year", 1, 52, 1)

# Lag Features

st.subheader("Lag Features (Important for Forecasting)")
lag1 = st.number_input("Yesterday Sales (Lag_1)", value=50)
lag7 = st.number_input("Last Week Sales (Lag_7)", value=50)
rolling7 = st.number_input("7-day Avg Sales", value=50)

# Region

region = st.selectbox("Region", ["North","South","East","West"])

# ------------------- PREDICTION -------------------

if st.button("Predict Sales"):

```
input_dict = {
    'Store_ID': store,
    'Item_ID': item,
    'Promotion': promotion,
    'Holiday': holiday,
    'Temperature': temp,
    'Fuel_Price': fuel,
    'Month': month,
    'Day': day,
    'Day_of_Week': dow,
    'Week_of_Year': week,
    'Lag_1': lag1,
    'Lag_7': lag7,
    'Rolling_Mean_7': rolling7
}

# One-hot encoding for region
for col in columns:
    if 'Region_' in col:
        input_dict[col] = 1 if col == f"Region_{region}" else 0

input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=columns, fill_value=0)

prediction = model.predict(input_df)[0]

st.success(f"📊 Predicted Sales: {prediction:.2f}")

# Chart
chart_data = pd.DataFrame({
    "Metric": ["Lag_1", "Lag_7", "Rolling Avg", "Prediction"],
    "Value": [lag1, lag7, rolling7, prediction]
})

st.bar_chart(chart_data.set_index("Metric"))
```

# ------------------- BATCH PREDICTION -------------------

st.markdown("---")
st.subheader("📂 Batch Prediction")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
data = pd.read_csv(file)

```
data = data.reindex(columns=columns, fill_value=0)

preds = model.predict(data)
data['Predicted_Sales'] = preds

st.write(data.head())

csv = data.to_csv(index=False).encode('utf-8')
st.download_button("Download Results", csv, "forecast_results.csv")
```
