import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
import os


from azure.storage.blob import BlobServiceClient
raw_folder = "data/raw"
processed_path = "data/processed/stock_data.csv"

os.makedirs("data/processed", exist_ok=True)

all_dataframes = []

for file_name in os.listdir(raw_folder):
    if file_name.endswith(".json"):
        file_path = os.path.join(raw_folder, file_name)

        with open(file_path, "r") as f:
            data = json.load(f)

        if "Time Series (Daily)" in data:
            time_series = data["Time Series (Daily)"]

            df = pd.DataFrame.from_dict(time_series, orient="index")
            df = df.reset_index()
            df = df.rename(columns={"index": "date"})
            df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

            for col in df.columns:
                if col != "date":
                    df[col] = pd.to_numeric(df[col], errors="coerce")
            price_columns = ["1. open", "2. high", "3. low", "4. close"]

            for col in price_columns:
                df[col] = df[col].round(2)

            df["price_change"] = df["4. close"] - df["1. open"]
            df["daily_return"] = (df["price_change"] / df["1. open"]) * 100

            df["price_change"] = df["price_change"].round(2)
            df["daily_return"] = df["daily_return"].round(2)

            symbol = file_name.split("_")[0]
            df["symbol"] = symbol
           

            all_dataframes.append(df)

if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    # Remove duplicate stock-date records
    combined_df.drop_duplicates(
        subset=["symbol", "date"],
        keep="last",
        inplace=True
    )
    # Sort by symbol and date for better organization
    combined_df.sort_values(by=["symbol", "date"], inplace=True)

    if os.path.exists(processed_path):
        existing_df = pd.read_csv(processed_path)

        # If old file does not have symbol column, rebuild from scratch
        if "symbol" not in existing_df.columns:
            print("Old processed file format detected. Rebuilding dataset...")
            updated_df = combined_df
        else:
            existing_df["date"] = pd.to_datetime(existing_df["date"])

            new_data = combined_df.merge(
                existing_df[["symbol", "date"]],
                on=["symbol", "date"],
                how="left",
                indicator=True
            )

            new_data = new_data[new_data["_merge"] == "left_only"].drop(columns=["_merge"])
            updated_df = pd.concat([existing_df, new_data], ignore_index=True)
    else:
        updated_df = combined_df
    
    updated_df.to_csv(processed_path, index=False)
    print("Transformation complete ")

    #try:
        # Save locally
       # updated_df.to_csv(processed_path, index=False)
       # print("Transformation complete ")

        # Upload to Azure Blob Storage
       # connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        #if not connection_string:
         #   raise ValueError("Azure connection string not set.")

        #blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        #container_name = "processed-data"
        #blob_name = "stock_data.csv"

        # Create container if it doesn't exist
        #container_client = blob_service_client.get_container_client(container_name)
        #try:
         #   container_client.create_container()
        #except Exception:
         #   pass  # container already exists

        # Upload file
        #with open(processed_path, "rb") as data_file:
         #   blob_client = blob_service_client.get_blob_client(
          #      container=container_name,
           #     blob=blob_name
            #)
            #blob_client.upload_blob(data_file, overwrite=True)

        #print("Uploaded to Azure Blob Storage")

    #except PermissionError:
        #print("Could not save file. Please close stock_data.csv and try again ❌")

    #except Exception as e:
        #print("Azure upload failed", e)
        #if the file is locked, we skip saving and print an error message. The pipeline will not crash, allowing for a graceful 
        # failure and the opportunity to fix the issue before rerunning.
else:
    print("No valid raw data found ")