
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
