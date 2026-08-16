# Databricks notebook source
from pyspark.sql.functions import col, ceil, lit, when, coalesce

# 1. Load Silver Tables
sales = spark.table("workforce_ai.silver.silver_hourly_sales")
weather = spark.table("workforce_ai.silver.silver_weather_daily")
holidays = spark.table("workforce_ai.silver.silver_bank_holidays")

# 2. Join Sales + Weather + Holidays
joined_df = (
    sales
    .join(weather, sales.sales_date == weather.weather_date, "left")
    .join(holidays, sales.sales_date == holidays.holiday_date, "left")
    .withColumn("is_bank_holiday", when(col("holiday_name").isNotNull(), 1).otherwise(0))
    .withColumn("is_weekend", when(col("day_of_week").isin([1, 7]), 1).otherwise(0))
    # Temporary fallback: using actual transaction count as predicted count until ML model runs
    .withColumn("predicted_transactions", col("transaction_count")) 
)

# 3. Create Gold Demand Forecast
gold_forecast = (
    joined_df
    .withColumn("required_headcount", ceil(col("predicted_transactions") / lit(8)))
    .select(
        "sales_hour",
        "sales_date",
        "hour_of_day",
        "transaction_count",
        "predicted_transactions",
        "required_headcount",
        coalesce(col("mean_temp"), lit(15.0)).alias("mean_temp"),
        coalesce(col("precipitation"), lit(0.0)).alias("precipitation"),
        "is_bank_holiday",
        "is_weekend"
    )
)

# 4. Save to Gold
gold_forecast.write.mode("overwrite").saveAsTable("workforce_ai.gold.gold_demand_forecast")