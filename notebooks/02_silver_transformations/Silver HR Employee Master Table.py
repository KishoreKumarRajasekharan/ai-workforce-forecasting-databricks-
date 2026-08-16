# Databricks notebook source
from pyspark.sql.functions import concat, lit, rand, col, when 

hr = spark.table("workforce_ai.bronze.bronze_hr_employees")

silver_hr = (
    hr
    .withColumnRenamed("EmployeeNumber", "employee_id")
    .withColumn("employee_name", concat(lit("Employee_"), col("employee_id")))
    .withColumn(
        "employment_type",
        when(rand() < 0.5, "Full-time")
        .when(rand() < 0.8, "Part-time")
        .otherwise("Zero-hours")
    )
    .withColumn(
        "contract_min_hours",
        when(col("employment_type") == "Full-time", lit(35))
        .when(col("employment_type") == "Part-time", lit(12))
        .otherwise(lit(0))
    )
    .withColumn(
        "contract_max_hours",
        when(col("employment_type") == "Full-time", lit(48))
        .when(col("employment_type") == "Part-time", lit(30))
        .otherwise(lit(20))
    )
    .withColumn(
        "base_hourly_rate",
        when(col("Age") < 18, lit(7.55))
        .when((col("Age") >= 18) & (col("Age") <= 20), lit(10.00))
        .when((col("Age") >= 21) & (col("Age") <= 22), lit(12.21))
        .otherwise(lit(12.75))
    )
    .withColumn(
        "age_tier",
        when(col("Age") < 18, "Under 18")
        .when((col("Age") >= 18) & (col("Age") <= 20), "18-20")
        .when((col("Age") >= 21) & (col("Age") <= 22), "21-22")
        .otherwise("23+")
    )
    .select(
        "employee_id",
        "employee_name",
        "Age",
        "age_tier",
        "Department",
        "JobRole",
        "employment_type",
        "contract_min_hours",
        "contract_max_hours",
        "base_hourly_rate",
        "OverTime",
        "TotalWorkingYears",
        "YearsAtCompany",
        "Attrition"
    )
)

silver_hr.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_hr_employees"
)