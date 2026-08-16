# Business Rules

## 1. Overview

This document explains the business rules and assumptions used in the AI Workforce Forecasting and Labour Cost Optimisation project.

These rules are used to convert demand forecasts into staffing requirements, create employee shift plans and calculate labour cost KPIs.

---

## 2. Demand Calculation

Retail demand is calculated using hourly transaction volume.

The main demand target is:

​
transaction_count

Revenue is also calculated as:

​
sales_amount = Quantity * UnitPrice

Hourly revenue is calculated by aggregating sales amount by hour.

---

## 3. Forecasting Target

The machine learning model predicts:

​
predicted_transactions

This represents the expected number of customer transactions in each hour.

---

## 4. Demand to Headcount Rule

Forecasted demand is converted into required employees using a Transactions Per Labour Hour rule.

​
required_headcount = CEIL(predicted_transactions / target_transactions_per_labour_hour)

Default assumption:

​
target_transactions_per_labour_hour = 8

Example:

​
Predicted transactions = 30
Target transactions per labour hour = 8
required_headcount = CEIL(30 / 8)
required_headcount = 4 employees

---

## 5. Shift Windows

The project uses four fixed shift windows.

| Shift Type | Start Hour | End Hour |
|---|---:|---:|
| Morning | 08:00 | 12:00 |
| Afternoon | 12:00 | 16:00 |
| Evening | 16:00 | 20:00 |
| Night | 20:00 | 00:00 |

Each shift is assumed to be 4 hours long.

---

## 6. Employee Employment Types

Employees are assigned one of the following synthetic employment types:

| Employment Type | Min Hours | Max Hours |
|---|---:|---:|
| Full-time | 35 | 48 |
| Part-time | 12 | 30 |
| Zero-hours | 0 | 20 |

These values are used to simulate contract-based scheduling limits.

---

## 7. Wage Rate Rules

Hourly wage is estimated using employee age tier.

Example assumptions:

| Age Tier | Base Hourly Rate |
|---|---:|
| Under 18 | £7.55 |
| 18-20 | £10.00 |
| 21-22 | £12.21 |
| 23+ | £12.75 |

These values are simplified assumptions for portfolio demonstration purposes.

---

## 8. Employee Availability Rules

Synthetic availability is generated based on employment type.

Example assumptions:

| Employment Type | Available Start | Available End |
|---|---:|---:|
| Full-time | 08:00 | 22:00 |
| Part-time | 10:00 | 20:00 |
| Zero-hours | 12:00 | 18:00 |

An employee can only be assigned to a shift if:

​
is_available = 1
available_start_hour <= shift_start_hour
available_end_hour >= shift_end_hour

---

## 9. Skill-Based Scheduling Rules

Employees are ranked for shift assignment using:

1. Higher skill rating first
2. Lower hourly wage second

This means the model gives priority to more skilled employees, while also considering labour cost efficiency.

---

## 10. Shift Coverage Rules

Each shift should ideally include:

- At least 1 shift lead
- At least 1 first aider

The project checks this using:

​
has_shift_lead = 1 if shift_lead_count >= 1
has_first_aider = 1 if first_aider_count >= 1

---

## 11. Weekly Compliance Rules

The project checks if employees exceed:

1. Their contract maximum weekly hours
2. The 48-hour weekly working limit

Rules:

​
exceeds_contract_max = 1 if weekly_scheduled_hours > contract_max_hours
exceeds_48_hour_limit = 1 if weekly_scheduled_hours > 48

---

## 12. Time and Attendance Rules

Actual attendance is simulated using scheduled shift times.

Example assumptions:

​
actual_clock_in = scheduled_start_ts + 5 minutes
actual_clock_out = scheduled_end_ts - 3 minutes
actual_break_minutes = 30

This creates simple actual hours variation for dashboard calculation.

---

## 13. Labour Cost Calculation

Scheduled labour cost is calculated as:

​
scheduled_labour_cost = scheduled_hours * base_hourly_rate

Actual labour cost is calculated as:

​
actual_labour_cost = actual_hours * base_hourly_rate

---

## 14. Labour Dashboard KPI Rules

### Labour Cost Percentage

​
labour_cost_percentage = actual_labour_cost / daily_revenue * 100

### Labour Cost Variance

​
labour_cost_variance_amount = actual_labour_cost - scheduled_labour_cost

### Hours Variance

​
hours_variance = actual_hours - scheduled_hours

### Transactions Per Labour Hour

​
transactions_per_labour_hour = daily_transactions / actual_hours

---

## 15. Project Assumptions

This project uses simplified business rules for demonstration purposes.

In a real-world implementation, the following would need to be configured based on business policy:

- Actual employee contracts
- Real wage rates
- Overtime rules
- Store opening hours
- Break policies
- Employee preferences
- Local labour regulations
- Payroll system rules
- HRIS data structure
