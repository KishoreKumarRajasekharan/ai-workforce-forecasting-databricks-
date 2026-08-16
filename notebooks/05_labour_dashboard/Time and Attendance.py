# Databricks notebook source
from pyspark.sql.functions import expr, when, col, lit, rand

shift_plan = spark.table("workforce_ai.gold.gold_shift_plan")

attendance = (
    shift_plan
    .withColumn(
        "scheduled_start_ts",
        expr("to_timestamp(concat(sales_date, ' ', shift_start_hour, ':00:00'))")
    )
    .withColumn(
        "scheduled_end_ts",
        expr("to_timestamp(concat(sales_date, ' ', shift_end_hour, ':00:00'))")
    )
    .withColumn(
        "actual_clock_in",
        expr("scheduled_start_ts + interval 5 minutes")
    )
    .withColumn(
        "actual_clock_out",
        expr("scheduled_end_ts - interval 3 minutes")
    )
    .withColumn("actual_break_minutes", lit(30))
    .withColumn(
        "early_clock_in_flag",
        when(col("actual_clock_in") < col("scheduled_start_ts"), lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "geofence_verified",
        when(rand() < 0.95, lit(1)).otherwise(lit(0))
    )
)

attendance.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_time_attendance"
)