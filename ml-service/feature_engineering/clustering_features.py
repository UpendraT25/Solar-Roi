import pandas as pd


df = pd.read_csv(
    "../datasets/adoption_dataset.csv"
)


# Regional energy intensity

df["energy_intensity"] = (
    df["total_consumption"] /
    (
        df["population"]
        if "population" in df.columns
        else 1000000
    )
)


# Solar efficiency score

df["solar_efficiency_index"] = (
    df["solar_performance_score"] *
    df["irradiance"]
)


OUTPUT_PATH = (
    "../datasets/clustering_dataset.csv"
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("Clustering dataset created successfully.")