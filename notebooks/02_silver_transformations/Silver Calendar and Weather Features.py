# Databricks notebook source
from pyspark.sql.functions import col
weather = spark.table("workforce_ai.bronze.bronze_weather")

silver_weather = (
    weather
    .select(
        col("weather_date"),
        col("mean_temp").cast("double"),
        col("min_temp").cast("double"),
        col("max_temp").cast("double"),
        col("precipitation").cast("double"),
        col("sunshine").cast("double"),
        col("cloud_cover").cast("double")
    )
)

silver_weather.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_weather_daily"
)