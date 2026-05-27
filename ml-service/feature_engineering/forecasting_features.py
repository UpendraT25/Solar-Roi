import pandas as pd


df = pd.read_csv(
    "../datasets/clustering_dataset.csv"
)


# Lag features

df["lag_1"] = (
    df["total_consumption"].shift(1)
)

df["lag_7"] = (
    df["total_consumption"].shift(7)
)


# Rolling averages

df["rolling_mean_7"] = (
    df["total_consumption"]
    .rolling(7)
    .mean()
)

df["rolling_mean_30"] = (
    df["total_consumption"]
    .rolling(30)
    .mean()
)


df = df.bfill()


OUTPUT_PATH = (
    "../datasets/final_master_dataset.csv"
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("Final forecasting dataset created.")