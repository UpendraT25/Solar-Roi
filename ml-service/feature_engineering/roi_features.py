import pandas as pd
import numpy as np


df = pd.read_csv(
    "../datasets/master_dataset.csv"
)


# -----------------------------------
# SYNTHETIC BUSINESS FEATURES
# -----------------------------------


np.random.seed(42)


# Installation cost

df["installation_cost"] = np.random.randint(
    200000,
    800000,
    size=len(df)
)


# Electricity tariff

df["tariff_rate"] = np.random.uniform(
    5,
    12,
    size=len(df)
)


# Annual savings

df["annual_savings"] = (
    df["AC_POWER"] *
    365 *
    df["tariff_rate"]
)


# Maintenance cost

df["maintenance_cost"] = (
    df["installation_cost"] * 0.02
)


# Subsidy

df["subsidy"] = (
    df["installation_cost"] * 0.20
)


# Net installation cost

df["net_installation_cost"] = (
    df["installation_cost"] -
    df["subsidy"]
)


# -----------------------------------
# ROI CALCULATION
# -----------------------------------

df["roi"] = (
    (
        df["annual_savings"] -
        df["maintenance_cost"]
    )
    /
    df["net_installation_cost"]
) * 100


# -----------------------------------
# PAYBACK PERIOD
# -----------------------------------

df["payback_period"] = (
    df["net_installation_cost"] /
    (
        df["annual_savings"] + 1
    )
)


# -----------------------------------
# SAVE DATASET
# -----------------------------------

OUTPUT_PATH = (
    "../datasets/roi_dataset.csv"
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("ROI dataset created successfully.")