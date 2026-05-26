import pandas as pd
import numpy as np


DATA_PATH = "../datasets/electricity/india_electricity_consumption.csv"


print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)


# -----------------------------------
# DATE PROCESSING
# -----------------------------------

print("\nProcessing date column...")

df["Dates"] = pd.to_datetime(df["Dates"])


# -----------------------------------
# SORTING
# -----------------------------------

df = df.sort_values("Dates")


# -----------------------------------
# MISSING VALUES
# -----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# Fill missing values

df = df.ffill()


# -----------------------------------
# FEATURE ENGINEERING
# -----------------------------------

print("\nCreating time-series features...")


df["year"] = df["Dates"].dt.year
df["month"] = df["Dates"].dt.month
df["day"] = df["Dates"].dt.day
df["day_of_week"] = df["Dates"].dt.dayofweek
df["quarter"] = df["Dates"].dt.quarter


# -----------------------------------
# NATIONAL TOTAL CONSUMPTION
# -----------------------------------

state_columns = df.columns[1:-5]

df["total_consumption"] = df[state_columns].sum(axis=1, numeric_only=True)


# -----------------------------------
# DAILY GROWTH RATE
# -----------------------------------

df["daily_growth_rate"] = (
    df["total_consumption"].pct_change() * 100
)


# -----------------------------------
# ROLLING AVERAGES
# -----------------------------------

df["rolling_7_day_avg"] = (
    df["total_consumption"]
    .rolling(window=7)
    .mean()
)

df["rolling_30_day_avg"] = (
    df["total_consumption"]
    .rolling(window=30)
    .mean()
)


# -----------------------------------
# FILL AGAIN
# -----------------------------------

df = df.ffill()


# -----------------------------------
# DATA SUMMARY
# -----------------------------------

print("\nProcessed Dataset Shape:")
print(df.shape)

print("\nProcessed Columns:")
print(df.columns)

print("\nStatistics:")
print(df.describe())


# -----------------------------------
# SAVE CLEAN DATASET
# -----------------------------------

OUTPUT_PATH = (
    "../datasets/electricity/"
    "cleaned_india_electricity.csv"
)

df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned dataset saved successfully.")