# Databricks notebook source
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml import Pipeline
from pyspark.sql.functions import col

df = spark.table("workforce_ai.gold.gold_demand_features").dropna()

feature_cols = [
    "hour_of_day",
    "day_of_week",
    "month",
    "mean_temp",
    "precipitation",
    "is_bank_holiday",
    "is_weekend",
    "is_payday_marker"
]

assembler = VectorAssembler(
    inputCols=feature_cols,
    outputCol="features"
)

rf = RandomForestRegressor(
    featuresCol="features",
    labelCol="transaction_count",
    predictionCol="predicted_transactions",
    numTrees=50,
    maxDepth=5,
    seed=42
)

pipeline = Pipeline(stages=[assembler, rf])

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

model = pipeline.fit(train_df)

predictions = model.transform(test_df)

display(predictions.select(
    "sales_hour",
    "transaction_count",
    "predicted_transactions",
    "hour_of_day",
    "day_of_week",
    "mean_temp",
    "precipitation",
    "is_bank_holiday"
))