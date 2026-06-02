# Weather API Pipeline

This project extracts current weather data from the OpenWeather API for major African cities, transforms the JSON responses into a Pandas DataFrame, performs basic data quality checks, and loads the results into PostgreSQL.

## Pipeline Flow

OpenWeather API → Python Requests → Pandas DataFrame → PostgreSQL

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

## Technologies Used

- Python
- Requests
- Pandas
- PostgreSQL
- SQLAlchemy
- python-dotenv

## Data Quality Checks

The script checks:

- Column data types
- Null values
- Duplicate rows

## Database Table

The data is loaded into a PostgreSQL table called:

weather_data

## Environment Variables

The project uses a .env file for API and database credentials.

Required variables:

OPENWEATHER_API_KEY=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=

The .env file is ignored by Git and should not be pushed to GitHub.