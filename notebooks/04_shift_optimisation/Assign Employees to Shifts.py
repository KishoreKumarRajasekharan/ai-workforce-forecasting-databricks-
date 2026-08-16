# Databricks notebook source
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, col, dayofweek

# 1. Load Tables
shift_demand = spark.table("workforce_ai.gold.gold_shift_demand")
employees = spark.table("workforce_ai.silver.silver_hr_employees")
availability = spark.table("workforce_ai.silver.silver_employee_availability")
skills = spark.table("workforce_ai.silver.silver_employee_skills")

# 2. Build Candidate Pool (Includes all shared columns in join arrays to prevent ambiguity)
candidate_pool = (
    shift_demand
    .withColumn("day_of_week", dayofweek(col("sales_date")))
    .join(availability, ["day_of_week"], "inner")
    # Added 'employment_type' to the join list here:
    .join(employees, ["employee_id", "employee_name", "employment_type"], "inner")
    # Included 'JobRole' in the join list here:
    .join(skills, ["employee_id", "employee_name", "JobRole"], "inner")
    .filter(col("is_available") == 1)
    .filter(col("available_start_hour") <= col("shift_start_hour"))
    .filter(col("available_end_hour") >= col("shift_end_hour"))
)

# 3. Rank Candidates by Highest Skill Rating & Lowest Cost
w = Window.partitionBy(
    "sales_date", "shift_type"
).orderBy(
    col("skill_rating").desc(),
    col("base_hourly_rate").asc()
)

ranked_candidates = candidate_pool.withColumn(
    "employee_rank",
    row_number().over(w)
)

# 4. Generate Final Gold Shift Plan
gold_shift_plan = (
    ranked_candidates
    .filter(col("employee_rank") <= col("total_required_headcount"))
    .withColumn(
        "scheduled_hours",
        col("shift_end_hour") - col("shift_start_hour")
    )
    .withColumn(
        "scheduled_labour_cost",
        col("scheduled_hours") * col("base_hourly_rate")
    )
    .select(
        "sales_date",
        "shift_type",
        "shift_start_hour",
        "shift_end_hour",
        "employee_id",
        "employee_name",
        "JobRole",
        "employment_type",
        "base_hourly_rate",
        "skill_rating",
        "is_shift_lead",
        "is_first_aider",
        "scheduled_hours",
        "scheduled_labour_cost"
    )
)

# 5. Save to Gold Schema
gold_shift_plan.write.mode("overwrite").saveAsTable(
    "workforce_ai.gold.gold_shift_plan"
)