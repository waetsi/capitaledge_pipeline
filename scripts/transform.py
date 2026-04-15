import json
import pandas as pd
import os

# Load latest file
files = os.listdir("data/raw")
latest_file = sorted(files)[-1]

file_path = f"data/raw/{latest_file}"

with open(file_path, "r") as f:
    data = json.load(f)

time_series = data["Time Series (Daily)"]

df = pd.DataFrame.from_dict(time_series, orient="index")

df = df.reset_index()
df = df.rename(columns={"index": "date"})

df["date"] = pd.to_datetime(df["date"])

for col in df.columns:
    if col != "date":
        df[col] = pd.to_numeric(df[col], errors="coerce")

df.sort_values(by="date", inplace=True)

# Incremental loading
os.makedirs("data/processed", exist_ok=True)
processed_path = "data/processed/stock_data.csv"

if os.path.exists(processed_path):
    existing_df = pd.read_csv(processed_path)
    existing_df["date"] = pd.to_datetime(existing_df["date"])

    new_data = df[~df["date"].isin(existing_df["date"])]

    updated_df = pd.concat([existing_df, new_data])
else:
    updated_df = df

updated_df.to_csv(processed_path, index=False)

print("Transformation complete ✅")