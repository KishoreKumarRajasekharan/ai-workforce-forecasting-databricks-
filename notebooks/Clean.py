# Databricks notebook source
bronze_hr = (
    hr_df
    .withColumn("EmployeeNumber", col("EmployeeNumber").cast("int"))
    .withColumn("Age", col("Age").cast("int"))
    .withColumn("DailyRate", col("DailyRate").cast("double"))
)

bronze_hr.write.mode("overwrite").saveAsTable(
    "workforce_ai.bronze.bronze_hr_employees"
)