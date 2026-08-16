# Databricks notebook source
from pyspark.sql.functions import rand, when, lit 

employees = spark.table("workforce_ai.silver.silver_hr_employees")

silver_skills = (
    employees
    .select("employee_id", "employee_name", "JobRole")
    .withColumn(
        "is_shift_lead",
        when(rand() < 0.20, lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "is_first_aider",
        when(rand() < 0.25, lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "can_open_store",
        when(rand() < 0.30, lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "can_close_store",
        when(rand() < 0.30, lit(1)).otherwise(lit(0))
    )
    .withColumn(
        "skill_rating",
        when(rand() < 0.25, lit(5))
        .when(rand() < 0.50, lit(4))
        .when(rand() < 0.75, lit(3))
        .otherwise(lit(2))
    )
)

silver_skills.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_employee_skills"
)