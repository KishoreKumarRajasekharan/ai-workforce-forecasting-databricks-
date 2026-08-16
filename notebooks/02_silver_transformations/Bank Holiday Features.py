# Databricks notebook source
from pyspark.sql.functions import col

holidays = spark.table("workforce_ai.bronze.bronze_bank_holidays")

silver_holidays = (
    holidays
    .select(
        col("holiday_date"),
        col("title").alias("holiday_name"), 
        col("notes").alias("type_of_holiday") 
    )
    .dropDuplicates(["holiday_date"])
)

silver_holidays.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_bank_holidays"
)