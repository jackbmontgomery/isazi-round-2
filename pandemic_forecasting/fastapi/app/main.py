from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd

app = FastAPI()
origins = [
    "http://nuxt:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable to store the data
data = None

@app.on_event("startup")
async def startup_event():
    global data
    soup = BeautifulSoup(requests.get("https://www.worldometers.info/coronavirus/country/south-africa/").content, "html.parser")
    graph_cases_daily = soup.find("script", string=lambda t: 'Highcharts' and 'graph-cases-daily' in t if t else False).get_text()

    # Extraction of dates data
    dates_regex = re.compile(r"xAxis:\s*{\s*categories:\s*(\[[^\]]+\])")
    dates_matched = dates_regex.search(graph_cases_daily)
    dates = json.loads(dates_matched.group(1)) if dates_matched else []

    # Extraction of daily cases
    daily_cases_pattern = re.compile(r"series:\s*\[\s*{[^}]*name:\s*'Daily Cases'[^}]*data:\s*(\[[^\]]+\])")
    daily_cases_match = daily_cases_pattern.search(graph_cases_daily)

    # Cleaning data
    daily_cases_data = json.loads(daily_cases_match.group(1)) if daily_cases_match else []
    daily_cases_data = [0 if case is None else case for case in daily_cases_data]

    # Create a DataFrame from the two arrays
    data = pd.DataFrame({
        'date': pd.to_datetime(dates),
        'cases': daily_cases_data
    })

    # Set the 'date' column as the index
    data.set_index('date', inplace=True)
    data.index = pd.to_datetime(data.index)
    data = data.asfreq('D')

@app.get("/")
def read_root():
    global data
    # Convert the date index to a more human-readable string format (e.g., 'YYYY-MM-DD')
    data_copy = data.copy()
    data_copy.index = data_copy.index.strftime('%Y-%m-%d')
    
    # Return the JSON response
    return json.loads(data_copy.to_json(orient="index"))