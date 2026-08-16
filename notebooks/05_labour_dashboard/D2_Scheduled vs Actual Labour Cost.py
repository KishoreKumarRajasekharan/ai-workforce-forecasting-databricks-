# Databricks notebook source
dashboard = spark.table("workforce_ai.gold.gold_labour_dashboard")

display(
    dashboard.select(
        "sales_date",
        "scheduled_labour_cost",
        "actual_labour_cost"
    )
)