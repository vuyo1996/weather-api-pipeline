# Weather API Pipeline

This project extracts current weather data from the OpenWeather API for major African cities, transforms the JSON responses into a Pandas DataFrame, performs data quality checks, and loads the results into PostgreSQL.

The pipeline stores historical weather observations, allowing weather trends and city comparisons to be analyzed over time.

## Pipeline Flow

OpenWeather API  
→ JSON Response  
→ Python Requests  
→ Pandas DataFrame  
→ Data Validation  
→ PostgreSQL

## Cities Included

- Harare, Zimbabwe
- Lagos, Nigeria
- Nairobi, Kenya
- Cape Town, South Africa
- Cairo, Egypt
- Accra, Ghana
- Addis Ababa, Ethiopia
- Kigali, Rwanda
- Dakar, Senegal
- Casablanca, Morocco

## Project Structure

```text
weather-api-pipeline/
├── src/
│   └── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

## Technologies Used

- Python
- Requests
- Pandas
- PostgreSQL
- SQLAlchemy
- python-dotenv
- Python Logging

## Data Collected

The pipeline captures:

- City
- Country
- Temperature
- Feels Like Temperature
- Humidity
- Pressure
- Weather Condition
- Weather Description
- Wind Speed
- Weather Timestamp
- Load Timestamp

## Data Quality Checks

The pipeline performs:

- Null value checks
- Duplicate row checks
- Record count validation
- DataFrame shape validation

## Pipeline Features

- API error handling using `try/except`
- Request timeout protection
- Structured logging using Python's `logging` module
- Environment variable management using `python-dotenv`
- Historical data loading into PostgreSQL
- Automatic weather and load timestamps
- PostgreSQL integration using SQLAlchemy

## Database Table

Weather data is loaded into the following PostgreSQL table:

```sql
weather_data
```

The pipeline uses append mode, allowing historical weather observations to accumulate over time rather than replacing existing records.

## Environment Variables

The project uses a `.env` file to store API and database credentials.

Required variables:

```text
OPENWEATHER_API_KEY=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
```

The `.env` file is excluded from version control and should never be committed to GitHub.

## Example Analysis Questions

- Which city currently has the highest temperature?
- What is the average temperature across all cities?
- How many records exist for each country?
- What is the average temperature for each city?
- Which city has recorded the highest wind speed?

## Future Improvements

- Schedule automated pipeline runs
- Store weather forecasts in addition to current conditions
- Add database indexes for faster querying
- Containerize the pipeline with Docker
- Orchestrate pipeline execution with workflow tools such as Apache Airflow

## Author

Vuyo M.