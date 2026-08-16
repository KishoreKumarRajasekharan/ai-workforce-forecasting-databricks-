# Databricks notebook source
forecast = spark.table("workforce_ai.gold.gold_demand_forecast")

display(
    forecast.select(
        "sales_hour",
        "transaction_count",
        "predicted_transactions",
        "required_headcount"
    )
)