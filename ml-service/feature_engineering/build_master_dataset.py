import pandas as pd
import numpy as np


# -----------------------------------
# LOAD DATASETS
# -----------------------------------

print("Loading datasets...")


weather_df = pd.read_csv(
    "../datasets/weather/nasa_weather_india.csv"
)

electricity_df = pd.read_csv(
    "../datasets/electricity/cleaned_india_electricity.csv"
)

solar_df = pd.read_csv(
    "../datasets/solar_generation/cleaned_solar_generation.csv"
)


# -----------------------------------
# DATE CONVERSION
# -----------------------------------
weather_df["date"] = pd.to_datetime(
    weather_df["date"], format="%Y%m%d"
).dt.normalize()

electricity_df["Dates"] = pd.to_datetime(
    electricity_df["Dates"]
)

solar_df["DATE_TIME"] = pd.to_datetime(
    solar_df["DATE_TIME"]
)


# -----------------------------------
# CREATE DATE COLUMN
# -----------------------------------

solar_df["date"] = solar_df["DATE_TIME"].dt.date
solar_df["date"] = pd.to_datetime(
    solar_df["date"]
)

# -----------------------------------
# AGGREGATE SOLAR DATA DAILY
# -----------------------------------

print("Aggregating solar data...")


solar_daily = solar_df.groupby("date").agg({
    "AC_POWER": "mean",
    "DC_POWER": "mean",
    "IRRADIATION": "mean",
    "solar_performance_score": "mean"
}).reset_index()


# -----------------------------------
# MERGE WEATHER + SOLAR
# -----------------------------------

print("Merging weather and solar...")


weather_solar_df = pd.merge(
    weather_df,
    solar_daily,
    on="date",
    how="inner"
)
print("weather solar df")
print(weather_solar_df["date"])

# -----------------------------------
# MERGE ELECTRICITY
# -----------------------------------

print("Merging electricity data...")

print(weather_solar_df["date"])
print("electricity value of electricity")
print(electricity_df["Dates"])
master_df = pd.merge(
    weather_solar_df,
    electricity_df,
    left_on="date",
    right_on="Dates",
    how="inner"
)


# -----------------------------------
# DROP DUPLICATES
# -----------------------------------

master_df = master_df.drop_duplicates()


# -----------------------------------
# BASIC CLEANING
# -----------------------------------

master_df = master_df.ffill()


# -----------------------------------
# SAVE MASTER DATASET
# -----------------------------------

OUTPUT_PATH = (
    "../datasets/master_dataset.csv"
)

master_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nMaster dataset created successfully.")

print("\nShape:")
print(master_df.shape)

print("\nColumns:")
print(master_df.columns)