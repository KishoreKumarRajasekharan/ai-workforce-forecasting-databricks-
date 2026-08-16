# Databricks notebook source
from pyspark.sql.functions import when, lit, last_day, date_format
from pyspark.sql.functions import col

sales = spark.table("workforce_ai.silver.silver_hourly_sales")
weather = spark.table("workforce_ai.silver.silver_weather_daily")
holidays = spark.table("workforce_ai.silver.silver_bank_holidays")

gold_demand_features = (
    sales
    .join(weather, sales.sales_date == weather.weather_date, "left")
    .join(holidays, sales.sales_date == holidays.holiday_date, "left")
    .withColumn(
        "is_bank_holiday",
        when(col("holiday_date").isNotNull(), lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "is_weekend",
        when(col("day_of_week").isin([1, 7]), lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "is_payday_marker",
        when(
            (date_format(col("sales_date"), "d") == "25") |
            (col("sales_date") == last_day(col("sales_date"))),
            lit(1)
        ).otherwise(lit(0))
    )
    .select(
        "sales_hour",
        "sales_date",
        "hour_of_day",
        "day_of_week",
        "month",
        "hourly_revenue",
        "transaction_count",
        "units_sold",
        "mean_temp",
        "min_temp",
        "max_temp",
        "precipitation",
        "sunshine",
        "cloud_cover",
        "is_bank_holiday",
        "is_weekend",
        "is_payday_marker"
    )
)

gold_demand_features.write.mode("overwrite").saveAsTable(
    "workforce_ai.gold.gold_demand_features"
)