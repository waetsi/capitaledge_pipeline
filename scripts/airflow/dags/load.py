from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient

load_dotenv()

processed_path = "data/processed/stock_data.csv"

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
if not connection_string:
    raise ValueError("Azure connection string not set.")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "processed-data"
blob_name = "stock_data.csv"

container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
except Exception:
    pass

with open(processed_path, "rb") as data_file:
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    blob_client.upload_blob(data_file, overwrite=True)

print("Load complete ✅ Uploaded to Azure Blob Storage")