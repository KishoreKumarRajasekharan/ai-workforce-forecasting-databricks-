# Model Explanation

## 1. Overview

This document explains the machine learning approach used in the AI Workforce Forecasting and Labour Cost Optimisation project.

The model forecasts hourly retail demand using historical sales, weather and calendar-based features.

The forecast is then converted into required workforce headcount.

---

## 2. Forecasting Objective

The objective of the model is to predict hourly customer transaction demand.

Target variable:

​
transaction_count

The model predicts:

​
predicted_transactions

This output is used to estimate how many employees are required for each hour.

---

## 3. Input Dataset

The model uses the Gold demand feature table:

​
gold_demand_features

This table combines:

- Hourly sales data
- Weather data
- Bank holiday data
- Calendar features

---

## 4. Feature Variables

The model uses the following features:

| Feature | Description |
|---|---|
| hour_of_day | Hour of the day |
| day_of_week | Day of the week |
| month | Month number |
| mean_temp | Average temperature |
| precipitation | Rainfall level |
| is_bank_holiday | Bank holiday flag |
| is_weekend | Weekend flag |
| is_payday_marker | Payday marker flag |

---

## 5. Target Variable

The target variable is:

​
transaction_count

This represents the number of unique transactions in a specific hour.

---

## 6. Model Used

The baseline model used in this project is:

​
Random Forest Regressor

The model was selected because:

- It can handle non-linear relationships
- It works well with mixed numerical and categorical-style features
- It is easy to implement in Spark MLlib
- It provides a strong baseline for forecasting demand
- It is suitable for a portfolio project demonstration

---

## 7. Modelling Process

The modelling process follows these steps:

​
Load gold_demand_features table
Remove rows with missing values
Select feature columns
Use VectorAssembler to combine features
Split data into training and test sets
Train Random Forest Regressor
Generate predictions on test data
Save predicted transactions
Convert predictions into required headcount

---

## 8. Feature Engineering

The project creates time-based and external demand features.

### Time-Based Features

| Feature | Purpose |
|---|---|
| hour_of_day | Captures intraday trading patterns |
| day_of_week | Captures weekday vs weekend behaviour |
| month | Captures seasonal variation |
| is_weekend | Identifies weekend demand patterns |
| is_payday_marker | Captures possible pay-day demand increase |

### Weather Features

| Feature | Purpose |
|---|---|
| mean_temp | Captures temperature impact on demand |
| precipitation | Captures rainfall impact on demand |

### Holiday Features

| Feature | Purpose |
|---|---|
| is_bank_holiday | Captures demand changes during UK bank holidays |

---

## 9. Demand to Staffing Conversion

The model output is converted into required headcount using a business rule:

​
required_headcount = CEIL(predicted_transactions / 8)

The assumption is:

​
1 employee can handle 8 transactions per hour

Example:

​
Predicted transactions = 25
required_headcount = CEIL(25 / 8)
required_headcount = 4 employees

---

## 10. Model Output

The model output is stored in:

​
gold_demand_forecast

Important columns:

| Column | Description |
|---|---|
| sales_hour | Forecast hour |
| transaction_count | Actual transactions |
| predicted_transactions | Forecasted transactions |
| required_headcount | Estimated employees required |

---

## 11. Model Evaluation

This project currently uses a baseline modelling approach.

Recommended evaluation metrics for future improvement:

| Metric | Purpose |
|---|---|
| MAE | Average absolute prediction error |
| RMSE | Penalises larger prediction errors |
| R² Score | Explains variance captured by the model |
| MAPE | Percentage-based forecast error |

---

## 12. Limitations

The current model has some limitations:

- It uses public retail transaction data, not real store-level POS data
- Weather data is daily, not hourly
- Workforce records are synthetic
- Local events and promotions are not included
- The model is a baseline, not a production forecasting model
- No hyperparameter tuning has been applied yet

---

## 13. Future Improvements

Future improvements could include:

- Use Prophet or XGBoost for forecasting
- Add MLflow experiment tracking
- Add hyperparameter tuning
- Use time-series cross-validation
- Add local event and promotion data
- Add school holiday data
- Use real-time POS data
- Build store-level forecasting
- Compare multiple model types
- Add feature importance analysis

---

## 14. Business Value

The main value of the model is not only prediction.

The business value comes from connecting the forecast to operational decision-making:

​
Forecast demand → estimate required headcount → assign shifts → monitor labour cost

This helps business users make better staffing and cost control decisions.
