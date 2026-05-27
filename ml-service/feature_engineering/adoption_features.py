import pandas as pd
import numpy as np


df = pd.read_csv(
    "../datasets/roi_dataset.csv"
)


# -----------------------------------
# SYNTHETIC DEMOGRAPHIC FEATURES
# -----------------------------------


np.random.seed(42)


df["income"] = np.random.randint(
    200000,
    2500000,
    size=len(df)
)


df["urbanization_score"] = np.random.uniform(
    0,
    1,
    size=len(df)
)


# -----------------------------------
# SOLAR ADOPTION LOGIC
# -----------------------------------

conditions = (
    (df["income"] > 600000)
    &
    (df["roi"] > 15)
    &
    (df["urbanization_score"] > 0.5)
)


df["solar_adoption"] = np.where(
    conditions,
    1,
    0
)


# -----------------------------------
# SAVE
# -----------------------------------

OUTPUT_PATH = (
    "../datasets/adoption_dataset.csv"
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("Adoption dataset created successfully.")