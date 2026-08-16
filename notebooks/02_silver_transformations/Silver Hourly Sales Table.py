# Databricks notebook source
from pyspark.sql.functions import (
    col, date_trunc, sum as spark_sum, countDistinct, count, 
    to_date, hour, dayofweek, month
)

retail = spark.table("workforce_ai.bronze.bronze_retail_sales")

silver_hourly_sales = (
    retail
    .filter(col("Quantity") > 0)
    .filter(col("UnitPrice") > 0)
    .withColumn("sales_amount", col("Quantity") * col("UnitPrice"))
    .withColumn("sales_hour", date_trunc("hour", col("InvoiceDate")))
    .groupBy("sales_hour")
    .agg(
        spark_sum("sales_amount").alias("hourly_revenue"),
        count("*").alias("transaction_lines"),
        countDistinct("InvoiceNo").alias("transaction_count"),
        spark_sum("Quantity").alias("units_sold")
    )
    .withColumn("sales_date", to_date(col("sales_hour")))
    .withColumn("hour_of_day", hour(col("sales_hour")))
    .withColumn("day_of_week", dayofweek(col("sales_hour")))
    .withColumn("month", month(col("sales_hour")))
)

silver_hourly_sales.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_hourly_sales"
)