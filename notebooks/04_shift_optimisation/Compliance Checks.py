# Databricks notebook source
from pyspark.sql.functions import weekofyear, when, lit, col
from pyspark.sql.functions import sum as spark_sum

shift_plan = spark.table("workforce_ai.gold.gold_shift_plan")
employees = spark.table("workforce_ai.silver.silver_hr_employees")

weekly_hours = (
    shift_plan
    .withColumn("week_number", weekofyear(col("sales_date")))
    .groupBy("employee_id", "employee_name", "week_number")
    .agg(
        spark_sum("scheduled_hours").alias("weekly_scheduled_hours")
    )
    .join(
        employees.select(
            "employee_id",
            "contract_max_hours"
        ),
        "employee_id",
        "left"
    )
    .withColumn(
        "exceeds_contract_max",
        when(
            col("weekly_scheduled_hours") > col("contract_max_hours"),
            lit(1)
        ).otherwise(lit(0))
    )
    .withColumn(
        "exceeds_48_hour_limit",
        when(
            col("weekly_scheduled_hours") > 48,
            lit(1)
        ).otherwise(lit(0))
    )
)

weekly_hours.write.mode("overwrite").saveAsTable(
    "workforce_ai.gold.gold_weekly_compliance"
)