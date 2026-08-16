# Databricks notebook source
from pyspark.sql.functions import weekofyear, when, lit, col, countDistinct
from pyspark.sql.functions import sum as spark_sum  # Alias PySpark's sum to spark_sum

# 1. READ the Gold Shift Plan DataFrame into 'shift_plan'
shift_plan = spark.table("workforce_ai.gold.gold_shift_plan")

# 2. NOW shift_plan is a DataFrame, so .groupBy() works!
coverage_check = (
    shift_plan
    .groupBy("sales_date", "shift_type")
    .agg(
        spark_sum("is_shift_lead").alias("shift_lead_count"),
        spark_sum("is_first_aider").alias("first_aider_count"),
        countDistinct("employee_id").alias("scheduled_employee_count")
    )
    .withColumn(
        "has_shift_lead",
        when(col("shift_lead_count") >= 1, lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "has_first_aider",
        when(col("first_aider_count") >= 1, lit(1)).otherwise(lit(0))
    )
)

# 3. Save the Compliance Audit Table to Gold
coverage_check.write.mode("overwrite").saveAsTable(
    "workforce_ai.gold.gold_shift_coverage_check"
)