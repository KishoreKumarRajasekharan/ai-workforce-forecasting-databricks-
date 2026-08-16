# AI Workforce Forecasting & Labour Cost Optimisation

## Project Overview

This project demonstrates an end-to-end Databricks data pipeline for workforce forecasting and labour cost optimisation.

The project uses retail transaction data, weather data, UK bank holiday data and HR employee data to forecast hourly demand, estimate required staffing levels and calculate labour cost KPIs.

## Business Problem

Retail and hospitality businesses often face staffing challenges:

- Overstaffing during quiet periods
- Understaffing during peak hours
- High labour cost variance
- Poor visibility into workforce efficiency

This project shows how data and AI can support better workforce planning decisions.

## Datasets Used

The project uses the following public datasets:

1. Online Retail Dataset  
   https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset

2. London Weather Data  
   https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data

3. UK National Holidays Dataset  
   https://www.kaggle.com/datasets/shivd24coder/uk-national-holidays-dataset

4. HR Analytics Dataset  
   https://www.kaggle.com/datasets/rishikeshkonapure/hr-analytics-prediction

Synthetic workforce data is created for employee skills, availability, shifts and attendance.

## Tech Stack

- Databricks
- PySpark
- Delta Lake
- Spark SQL
- Spark MLlib
- Python
- Power BI / Databricks Dashboard
- GitHub

## Project Architecture

The project follows a Bronze, Silver and Gold lakehouse architecture.

### Bronze Layer

Raw CSV ingestion:

- bronze_retail_sales
- bronze_weather
- bronze_bank_holidays
- bronze_hr_employees

### Silver Layer

Cleaned and transformed tables:

- silver_hourly_sales
- silver_weather_daily
- silver_bank_holidays
- silver_hr_employees
- silver_employee_skills
- silver_employee_availability
- silver_time_attendance

### Gold Layer

Business output tables:

- gold_demand_features
- gold_demand_forecast
- gold_shift_plan
- gold_labour_dashboard

## Project Workflow

1. Upload raw CSV files into Databricks.
2. Ingest raw files into Bronze Delta tables.
3. Clean and transform data into Silver tables.
4. Join sales, weather and holiday data.
5. Create forecasting features.
6. Train a machine learning model to predict hourly demand.
7. Convert demand forecast into required headcount.
8. Simulate employee availability and shift allocation.
9. Calculate labour cost KPIs.
10. Build dashboard outputs.

## Key Outputs

- Hourly demand forecast
- Required headcount calculation
- Employee shift plan
- Scheduled vs actual labour hours
- Labour cost percentage
- Labour cost variance
- Transactions per labour hour

## Repository Structure
