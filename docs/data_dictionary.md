# Data Dictionary

## 1. Overview

This document explains the main tables and columns used in the AI Workforce Forecasting and Labour Cost Optimisation project.

The project uses Bronze, Silver and Gold layers.

---

# 2. Bronze Tables

## 2.1 bronze_retail_sales

Raw online retail transaction data.

| Column | Description |
|---|---|
| InvoiceNo | Unique invoice or transaction identifier |
| StockCode | Product stock code |
| Description | Product description |
| Quantity | Quantity purchased |
| InvoiceDate | Transaction date and time |
| UnitPrice | Unit price of the product |
| CustomerID | Customer identifier |
| Country | Customer country |

---

## 2.2 bronze_weather

Raw London weather dataset.

| Column | Description |
|---|---|
| date | Weather date |
| mean_temp | Average temperature |
| min_temp | Minimum temperature |
| max_temp | Maximum temperature |
| precipitation | Rainfall or precipitation level |
| sunshine | Sunshine duration |
| cloud_cover | Cloud cover measurement |

---

## 2.3 bronze_bank_holidays

Raw UK bank holiday dataset.

| Column | Description |
|---|---|
| date | Holiday date |
| holiday_name | Name of the holiday |
| type_of_holiday | Type or category of holiday |

---

## 2.4 bronze_hr_employees

Raw HR analytics employee data.

| Column | Description |
|---|---|
| EmployeeNumber | Unique employee identifier |
| Age | Employee age |
| Department | Employee department |
| JobRole | Employee job role |
| DailyRate | Daily pay rate |
| OverTime | Whether employee works overtime |
| TotalWorkingYears | Total years of work experience |
| YearsAtCompany | Years worked at the company |
| Attrition | Employee attrition status |

---

# 3. Silver Tables

## 3.1 silver_hourly_sales

Hourly aggregated sales and transaction table.

| Column | Description |
|---|---|
| sales_hour | Hour-level timestamp |
| sales_date | Date of sale |
| hour_of_day | Hour of day extracted from sales_hour |
| day_of_week | Day of week |
| month | Month number |
| hourly_revenue | Total revenue in that hour |
| transaction_lines | Number of transaction lines |
| transaction_count | Number of unique invoices in that hour |
| units_sold | Total units sold in that hour |

---

## 3.2 silver_weather_daily

Cleaned daily weather table.

| Column | Description |
|---|---|
| weather_date | Cleaned weather date |
| mean_temp | Average daily temperature |
| min_temp | Minimum daily temperature |
| max_temp | Maximum daily temperature |
| precipitation | Daily precipitation |
| sunshine | Sunshine measure |
| cloud_cover | Cloud cover measure |

---

## 3.3 silver_bank_holidays

Cleaned bank holiday table.

| Column | Description |
|---|---|
| holiday_date | Cleaned holiday date |
| holiday_name | Name of bank holiday |
| type_of_holiday | Holiday category |

---

## 3.4 silver_hr_employees

Cleaned and enriched employee master table.

| Column | Description |
|---|---|
| employee_id | Unique employee identifier |
| employee_name | Synthetic employee name |
| Age | Employee age |
| age_tier | Age category for wage and compliance logic |
| Department | Employee department |
| JobRole | Employee job role |
| employment_type | Full-time, part-time or zero-hours |
| contract_min_hours | Minimum contracted hours per week |
| contract_max_hours | Maximum contracted hours per week |
| base_hourly_rate | Estimated hourly wage rate |
| OverTime | Overtime status |
| TotalWorkingYears | Total work experience |
| YearsAtCompany | Tenure at company |
| Attrition | Attrition status |

---

## 3.5 silver_employee_skills

Synthetic employee skill matrix.

| Column | Description |
|---|---|
| employee_id | Employee identifier |
| employee_name | Employee name |
| JobRole | Job role |
| is_shift_lead | 1 if employee can act as shift lead |
| is_first_aider | 1 if employee is first-aid eligible |
| can_open_store | 1 if employee can open store |
| can_close_store | 1 if employee can close store |
| skill_rating | Synthetic skill rating from 1 to 5 |

---

## 3.6 silver_employee_availability

Synthetic employee availability table.

| Column | Description |
|---|---|
| employee_id | Employee identifier |
| employee_name | Employee name |
| employment_type | Employment type |
| day_of_week | Day of week number |
| day_name | Day name |
| available_start_hour | Employee available start hour |
| available_end_hour | Employee available end hour |
| is_available | 1 if employee is available |

---

## 3.7 silver_time_attendance

Synthetic actual attendance table.

| Column | Description |
|---|---|
| sales_date | Date of shift |
| employee_id | Employee identifier |
| employee_name | Employee name |
| scheduled_start_ts | Scheduled start timestamp |
| scheduled_end_ts | Scheduled end timestamp |
| actual_clock_in | Simulated actual clock-in timestamp |
| actual_clock_out | Simulated actual clock-out timestamp |
| actual_break_minutes | Simulated break duration |
| early_clock_in_flag | 1 if employee clocked in early |
| geofence_verified | 1 if location was verified |

---

# 4. Gold Tables

## 4.1 gold_demand_features

Final model training dataset.

| Column | Description |
|---|---|
| sales_hour | Hour-level timestamp |
| sales_date | Sales date |
| hour_of_day | Hour of day |
| day_of_week | Day of week |
| month | Month |
| hourly_revenue | Revenue in that hour |
| transaction_count | Actual transaction count |
| units_sold | Units sold |
| mean_temp | Average temperature |
| min_temp | Minimum temperature |
| max_temp | Maximum temperature |
| precipitation | Rainfall level |
| sunshine | Sunshine measure |
| cloud_cover | Cloud cover |
| is_bank_holiday | 1 if bank holiday |
| is_weekend | 1 if weekend |
| is_payday_marker | 1 if payday marker |

---

## 4.2 gold_demand_forecast

Forecasted demand and required headcount table.

| Column | Description |
|---|---|
| sales_hour | Hour-level timestamp |
| sales_date | Sales date |
| hour_of_day | Hour of day |
| transaction_count | Actual transaction count |
| predicted_transactions | Forecasted transaction count |
| required_headcount | Required employees for the hour |
| mean_temp | Average temperature |
| precipitation | Rainfall level |
| is_bank_holiday | Bank holiday flag |
| is_weekend | Weekend flag |

---

## 4.3 gold_shift_demand

Required headcount by shift.

| Column | Description |
|---|---|
| sales_date | Shift date |
| shift_type | Morning, Afternoon, Evening or Night |
| shift_start_hour | Shift start hour |
| shift_end_hour | Shift end hour |
| total_required_headcount | Required number of employees for the shift |

---

## 4.4 gold_shift_plan

Employee-level shift allocation table.

| Column | Description |
|---|---|
| sales_date | Shift date |
| shift_type | Shift category |
| shift_start_hour | Shift start hour |
| shift_end_hour | Shift end hour |
| employee_id | Employee identifier |
| employee_name | Employee name |
| JobRole | Job role |
| employment_type | Employment type |
| base_hourly_rate | Hourly wage |
| skill_rating | Skill score |
| is_shift_lead | Shift lead flag |
| is_first_aider | First aider flag |
| scheduled_hours | Planned shift duration |
| scheduled_labour_cost | Planned labour cost |

---

## 4.5 gold_weekly_compliance

Weekly employee compliance table.

| Column | Description |
|---|---|
| employee_id | Employee identifier |
| employee_name | Employee name |
| week_number | Week number |
| weekly_scheduled_hours | Total scheduled hours in the week |
| contract_max_hours | Contract maximum hours |
| exceeds_contract_max | 1 if scheduled hours exceed contract max |
| exceeds_48_hour_limit | 1 if scheduled hours exceed 48-hour limit |

---

## 4.6 gold_shift_coverage_check

Shift coverage validation table.

| Column | Description |
|---|---|
| sales_date | Shift date |
| shift_type | Shift category |
| shift_lead_count | Number of shift leads scheduled |
| first_aider_count | Number of first aiders scheduled |
| scheduled_employee_count | Total employees scheduled |
| has_shift_lead | 1 if at least one shift lead is scheduled |
| has_first_aider | 1 if at least one first aider is scheduled |

---

## 4.7 gold_labour_dashboard

Final dashboard table.

| Column | Description |
|---|---|
| sales_date | Business date |
| daily_revenue | Total daily revenue |
| daily_transactions | Total daily transactions |
| scheduled_hours | Total scheduled labour hours |
| actual_hours | Total actual labour hours |
| scheduled_labour_cost | Planned labour cost |
| actual_labour_cost | Actual labour cost |
| labour_cost_percentage | Labour cost as percentage of revenue |
| labour_cost_variance_amount | Difference between actual and scheduled labour cost |
| hours_variance | Difference between actual and scheduled hours |
| transactions_per_labour_hour | Productivity metric |
