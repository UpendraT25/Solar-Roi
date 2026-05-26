import requests
import pandas as pd

from config import (
    BASE_URL,
    PARAMETERS,
    START_YEAR,
    END_YEAR,
    COMMUNITY,
    FORMAT
)

from indian_locations import INDIAN_LOCATIONS


def fetch_nasa_data(city, lat, lon):

    params = {
        "parameters": ",".join(PARAMETERS),
        "community": COMMUNITY,
        "longitude": lon,
        "latitude": lat,
        "start": START_YEAR,
        "end": END_YEAR,
        "format": FORMAT
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    return data


def process_data(city, data):

    properties = data["properties"]["parameter"]

    irradiance = properties["ALLSKY_SFC_SW_DWN"]
    temperature = properties["T2M"]
    humidity = properties["RH2M"]
    wind_speed = properties["WS2M"]

    records = []

    for date in irradiance.keys():

        records.append({
            "city": city,
            "date": date,
            "irradiance": irradiance.get(date),
            "temperature": temperature.get(date),
            "humidity": humidity.get(date),
            "wind_speed": wind_speed.get(date)
        })

    return pd.DataFrame(records)


all_dataframes = []

for city, coords in INDIAN_LOCATIONS.items():

    print(f"Fetching data for {city}...")

    raw_data = fetch_nasa_data(
        city,
        coords["lat"],
        coords["lon"]
    )

    processed_df = process_data(city, raw_data)

    all_dataframes.append(processed_df)


final_df = pd.concat(all_dataframes)

print(final_df.head())

final_df.to_csv(
    "../../datasets/weather/nasa_weather_india.csv",
    index=False
)

print("NASA weather dataset saved successfully.")