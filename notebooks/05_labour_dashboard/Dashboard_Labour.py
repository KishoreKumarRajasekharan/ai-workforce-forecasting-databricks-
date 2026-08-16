# Databricks notebook source
dashboard = spark.table("workforce_ai.gold.gold_labour_dashboard")

display(
    dashboard.select(
        "sales_date",
        "labour_cost_percentage",
        "daily_revenue",
        "actual_labour_cost"
    )
)