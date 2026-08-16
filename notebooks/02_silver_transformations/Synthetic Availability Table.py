# Databricks notebook source
from pyspark.sql.functions import explode, array, when, col, lit, rand

employees = spark.table("workforce_ai.silver.silver_hr_employees")

weekday_df = spark.createDataFrame(
    [
        (1, "Sunday"),
        (2, "Monday"),
        (3, "Tuesday"),
        (4, "Wednesday"),
        (5, "Thursday"),
        (6, "Friday"),
        (7, "Saturday")
    ],
    ["day_of_week", "day_name"]
)

availability = (
    employees
    .select("employee_id", "employee_name", "employment_type")
    .crossJoin(weekday_df)
    .withColumn(
        "available_start_hour",
        when(col("employment_type") == "Full-time", lit(8))
        .when(col("employment_type") == "Part-time", lit(10))
        .otherwise(lit(12))
    )
    .withColumn(
        "available_end_hour",
        when(col("employment_type") == "Full-time", lit(22))
        .when(col("employment_type") == "Part-time", lit(20))
        .otherwise(lit(18))
    )
    .withColumn(
        "is_available",
        when(rand() < 0.85, lit(1)).otherwise(lit(0))
    )
)

availability.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_employee_availability"
)