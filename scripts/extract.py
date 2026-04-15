import requests
import json
import os
from datetime import datetime

API_KEY = "YOUR_API_KEY"
symbol = "AAPL"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

if "Time Series (Daily)" in data:
    os.makedirs("data/raw", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"data/raw/{symbol}_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Extraction complete ✅")
else:
    print("Invalid API response ❌")