import requests
import json
import os
import time
from dotenv import load_dotenv
import os

load_dotenv()
from datetime import datetime


API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

symbols = ["AAPL", "MSFT"]

os.makedirs("data/raw", exist_ok=True)

for symbol in symbols:
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" in data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f"data/raw/{symbol}_{timestamp}.json"

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"{symbol}: Extraction complete")
    else:
        print(f"{symbol}: Invalid API response")
        print(data)

    time.sleep(15)