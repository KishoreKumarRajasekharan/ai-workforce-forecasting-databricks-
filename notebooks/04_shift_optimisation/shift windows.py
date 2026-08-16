# Databricks notebook source
shift_windows = spark.createDataFrame(
    [
        ("Morning", 8, 12),
        ("Afternoon", 12, 16),
        ("Evening", 16, 20),
        ("Night", 20, 24)
    ],
    ["shift_type", "shift_start_hour", "shift_end_hour"]
)

shift_windows.write.mode("overwrite").saveAsTable(
    "workforce_ai.silver.silver_shift_windows"
)