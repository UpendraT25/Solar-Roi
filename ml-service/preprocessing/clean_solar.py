import pandas as pd
import numpy as np


# -----------------------------------
# LOAD DATASETS
# -----------------------------------

GEN_PATH = (
    "../datasets/solar_generation/"
    "Plant_1_Generation_Data.csv"
)

WEATHER_PATH = (
    "../datasets/solar_generation/"
    "Plant_1_Weather_Sensor_Data.csv"
)

print("Loading solar datasets...")

generation_df = pd.read_csv(GEN_PATH)

weather_df = pd.read_csv(WEATHER_PATH)


# -----------------------------------
# BASIC INFO
# -----------------------------------

print("\nGeneration Dataset:")
print(generation_df.head())

print("\nWeather Dataset:")
print(weather_df.head())


# -----------------------------------
# DATETIME CONVERSION
# -----------------------------------

generation_df["DATE_TIME"] = pd.to_datetime(
    generation_df["DATE_TIME"]
)

weather_df["DATE_TIME"] = pd.to_datetime(
    weather_df["DATE_TIME"]
)


# -----------------------------------
# MERGE DATASETS
# -----------------------------------

print("\nMerging datasets...")

merged_df = pd.merge(
    generation_df,
    weather_df,
    on=["DATE_TIME", "PLANT_ID"],
    how="inner"
)


# -----------------------------------
# SORTING
# -----------------------------------

merged_df = merged_df.sort_values("DATE_TIME")


# -----------------------------------
# MISSING VALUES
# -----------------------------------

print("\nMissing Values:")
print(merged_df.isnull().sum())

merged_df = merged_df.ffill()


# -----------------------------------
# FEATURE ENGINEERING
# -----------------------------------

print("\nCreating solar features...")


# Date features

merged_df["year"] = (
    merged_df["DATE_TIME"].dt.year
)

merged_df["month"] = (
    merged_df["DATE_TIME"].dt.month
)

merged_df["hour"] = (
    merged_df["DATE_TIME"].dt.hour
)


# -----------------------------------
# EFFICIENCY FEATURES
# -----------------------------------

merged_df["ac_dc_ratio"] = (
    merged_df["AC_POWER"] /
    (merged_df["DC_POWER"] + 1)
)


merged_df["temperature_difference"] = (
    merged_df["MODULE_TEMPERATURE"] -
    merged_df["AMBIENT_TEMPERATURE"]
)


merged_df["yield_per_dc_power"] = (
    merged_df["DAILY_YIELD"] /
    (merged_df["DC_POWER"] + 1)
)


# -----------------------------------
# ROLLING FEATURES
# -----------------------------------

merged_df["rolling_ac_power"] = (
    merged_df["AC_POWER"]
    .rolling(window=24)
    .mean()
)


# -----------------------------------
# SOLAR PERFORMANCE SCORE
# -----------------------------------

merged_df["solar_performance_score"] = (
    (
        merged_df["AC_POWER"] *
        merged_df["IRRADIATION"]
    )
    /
    (
        merged_df["MODULE_TEMPERATURE"] + 1
    )
)


# -----------------------------------
# FINAL CLEANING
# -----------------------------------

merged_df = merged_df.bfill()


# -----------------------------------
# SUMMARY
# -----------------------------------

print("\nProcessed Dataset Shape:")
print(merged_df.shape)

print("\nColumns:")
print(merged_df.columns)

print("\nStatistics:")
print(merged_df.describe())


# -----------------------------------
# SAVE CLEAN DATASET
# -----------------------------------

OUTPUT_PATH = (
    "../datasets/solar_generation/"
    "cleaned_solar_generation.csv"
)

merged_df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned solar dataset saved successfully.")