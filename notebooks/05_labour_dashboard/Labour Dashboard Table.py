# Databricks notebook source
from pyspark.sql.functions import sum as spark_sum, col 

sales = spark.table("workforce_ai.silver.silver_hourly_sales")
shift_plan = spark.table("workforce_ai.gold.gold_shift_plan")
attendance = spark.table("workforce_ai.silver.silver_time_attendance")

daily_sales = (
    sales
    .groupBy("sales_date")
    .agg(
        spark_sum("hourly_revenue").alias("daily_revenue"),
        spark_sum("transaction_count").alias("daily_transactions")
    )
)

daily_scheduled_labour = (
    shift_plan
    .groupBy("sales_date")
    .agg(
        spark_sum("scheduled_hours").alias("scheduled_hours"),
        spark_sum("scheduled_labour_cost").alias("scheduled_labour_cost")
    )
)

daily_actual_labour = (
    attendance
    .withColumn(
        "actual_hours",
        (
            col("actual_clock_out").cast("long") -
            col("actual_clock_in").cast("long")
        ) / 3600
    )
    .withColumn(
        "actual_labour_cost",
        col("actual_hours") * col("base_hourly_rate")
    )
    .groupBy("sales_date")
    .agg(
        spark_sum("actual_hours").alias("actual_hours"),
        spark_sum("actual_labour_cost").alias("actual_labour_cost")
    )
)

gold_labour_dashboard = (
    daily_sales
    .join(daily_scheduled_labour, "sales_date", "left")
    .join(daily_actual_labour, "sales_date", "left")
    .withColumn(
        "labour_cost_percentage",
        col("actual_labour_cost") / col("daily_revenue") * 100
    )
    .withColumn(
        "labour_cost_variance_amount",
        col("actual_labour_cost") - col("scheduled_labour_cost")
    )
    .withColumn(
        "hours_variance",
        col("actual_hours") - col("scheduled_hours")
    )
    .withColumn(
        "transactions_per_labour_hour",
        col("daily_transactions") / col("actual_hours")
    )
)

gold_labour_dashboard.write.mode("overwrite").saveAsTable(
    "workforce_ai.gold.gold_labour_dashboard"
)