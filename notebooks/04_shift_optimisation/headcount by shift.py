# Databricks notebook source
from pyspark.sql.functions import sum as spark_sum

forecast = spark.table("workforce_ai.gold.gold_demand_forecast")
windows = spark.table("workforce_ai.silver.silver_shift_windows")

shift_demand = (
    forecast
    .join(
        windows,
        (forecast.hour_of_day >= windows.shift_start_hour) &
        (forecast.hour_of_day < windows.shift_end_hour),
        "inner"
    )
    .groupBy(
        "sales_date",
        "shift_type",
        "shift_start_hour",
        "shift_end_hour"
    )
    .agg(
        spark_sum("required_headcount").alias("total_required_headcount")
    )
)

shift_demand.write.mode("overwrite").saveAsTable(
    "workforce_ai.gold.gold_shift_demand"
)