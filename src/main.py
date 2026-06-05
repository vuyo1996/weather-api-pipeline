import os
from datetime import datetime
from urllib.parse import quote_plus

import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", None)

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

engine = create_engine(
                         f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
                      )

cities = [
            "Harare,ZW",
            "Lagos,NG",
            "Nairobi,KE",
            "Cape Town,ZA",
            "Cairo,EG",
            "Accra,GH",
            "Addis Ababa,ET",
            "Kigali,RW",
            "Dakar,SN",
            "Casablanca,MA"
         ]

weather_records = []

for city in cities:

    params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
             }

    try:
        response = requests.get(
                                  BASE_URL,
                                  params=params,
                                  timeout=30
                               )
        
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as error:
        print(f"Failed to fetch weather data for {city}: {error}")
        continue

    weather_record = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "pressure": data["main"]["pressure"],
                        "weather_main": data["weather"][0]["main"],
                        "weather_description": data["weather"][0]["description"],
                        "wind_speed": data["wind"]["speed"],
                        "weather_timestamp": datetime.fromtimestamp(data["dt"])
                     }

    weather_records.append(weather_record)

print("\n")

weather_df = pd.DataFrame(weather_records)

weather_df["load_timestamp"] = datetime.now()

print(weather_df.dtypes)

print("\n")

print(weather_df)

print("\n")

print(f"Null values in each column:\n{weather_df.isnull().sum()}")

print("\n")

print(f"Duplicate rows:\n{weather_df.duplicated().sum()}")

weather_df.to_sql(
                    "weather_data",
                    engine,
                    if_exists="append",
                    index=False
                 )

print("\n")

print("Weather data loaded into PostgreSQL successfully.")