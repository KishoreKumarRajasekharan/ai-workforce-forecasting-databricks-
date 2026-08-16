
# Project Architecture

## 1. Overview

This project demonstrates an end-to-end workforce forecasting and labour cost optimisation solution using Databricks.

The goal is to forecast hourly retail demand, estimate required staffing levels, simulate employee shift allocation and calculate labour cost KPIs.

The project follows a Bronze, Silver and Gold lakehouse architecture.

---

## 2. Business Objective

Retail and hospitality businesses often face workforce planning challenges such as:

- Overstaffing during low-demand periods
- Understaffing during peak trading hours
- High labour cost variance
- Poor visibility into scheduled vs actual workforce cost
- Difficulty connecting demand forecasting with shift planning

This project shows how data engineering, machine learning and business rules can support better workforce planning decisions.

---

## 3. Data Sources

The project uses public datasets and synthetic workforce data.

| Dataset | Purpose |
|---|---|
| Online Retail Dataset | Historical transaction and sales demand |
| London Weather Dataset | External weather demand drivers |
| UK Bank Holidays Dataset | Calendar and holiday demand drivers |
| HR Analytics Dataset | Employee demographics and HR attributes |
| Synthetic Workforce Data | Employee skills, availability, shift plans and attendance records |

---

## 4. Lakehouse Architecture

The project is structured into three main data layers:
Raw CSV Files
v
Bronze Layer
v
Silver Layer
v
Gold Layer
v
Dashboard and Business Insights

---

## 5. Bronze Layer

The Bronze layer stores raw data ingested from CSV files.

Example tables:

| Table | Description |
|---|---|
| bronze_retail_sales | Raw retail transaction data |
| bronze_weather | Raw London weather data |
| bronze_bank_holidays | Raw UK bank holiday data |
| bronze_hr_employees | Raw HR employee data |

The purpose of the Bronze layer is to preserve the original source data with minimal transformation.

---

## 6. Silver Layer

The Silver layer contains cleaned, standardised and transformed data.

Example tables:

| Table | Description |
|---|---|
| silver_hourly_sales | Retail sales aggregated to hourly level |
| silver_weather_daily | Cleaned daily weather data |
| silver_bank_holidays | Cleaned holiday calendar table |
| silver_hr_employees | Cleaned employee master data |
| silver_employee_skills | Synthetic employee skill matrix |
| silver_employee_availability | Synthetic worker availability table |
| silver_time_attendance | Simulated actual clock-in and clock-out records |

The purpose of the Silver layer is to create business-ready data for analytics and modelling.

---

## 7. Gold Layer

The Gold layer contains final business outputs.

Example tables:

| Table | Description |
|---|---|
| gold_demand_features | Final modelling dataset with sales, weather and calendar features |
| gold_demand_forecast | Forecasted demand and required headcount |
| gold_shift_demand | Required employees by shift |
| gold_shift_plan | Employee-level shift allocation |
| gold_weekly_compliance | Weekly working hour compliance checks |
| gold_shift_coverage_check | Shift lead and first aider coverage checks |
| gold_labour_dashboard | Final labour cost KPI dashboard table |

The purpose of the Gold layer is to support business decisions and dashboard reporting.

---

## 8. Data Flow

The project follows this flow:

​
Online Retail Data
→ Bronze Retail Sales
→ Silver Hourly Sales
→ Gold Demand Features
→ Demand Forecast
→ Required Headcount
Weather Data
→ Bronze Weather
→ Silver Weather
→ Gold Demand Features
Bank Holiday Data
→ Bronze Bank Holidays
→ Silver Bank Holidays
→ Gold Demand Features
HR Data
→ Bronze HR Employees
→ Silver HR Employees
→ Skills and Availability
→ Shift Plan
Shift Plan + Attendance + Sales
→ Labour Dashboard

---

## 9. High-Level Solution Flow

​
Upload raw CSV files into Databricks
Create catalog and schemas
Ingest raw files into Bronze tables
Clean and transform data into Silver tables
Aggregate transactions into hourly demand
Join demand with weather and holiday features
Train a forecasting model
Convert forecasted demand into required headcount
Simulate employee skills and availability
Assign employees to shifts using business rules
Create attendance and compliance checks
Build labour cost dashboard table

---

## 10. Tools and Technologies

| Tool | Use |
|---|---|
| Databricks | Data engineering and ML workspace |
| PySpark | Data transformation and feature engineering |
| Delta Lake | Table storage |
| Spark SQL | Querying and dashboard outputs |
| Spark MLlib | Machine learning model |
| GitHub | Project version control and documentation |
| Power BI / Databricks Dashboard | Visualisation and reporting |

---

## 11. Final Output

The final output of the project is a labour analytics dashboard that can show:

- Forecasted hourly demand
- Required headcount
- Scheduled labour hours
- Actual labour hours
- Scheduled labour cost
- Actual labour cost
- Labour cost percentage
- Labour cost variance
- Transactions per labour hour
- Compliance and shift coverage checks

---

## 12. Project Limitations

Some workforce data was synthetically generated because public datasets do not usually include private employee rota, attendance, visa, payroll or availability information.

Synthetic data was created for:

- Employee skills
- Employee availability
- Shift assignment
- Clock-in and clock-out records
- Attendance variance

In a real implementation, this data would come from HR, payroll, rota and time-attendance syst
