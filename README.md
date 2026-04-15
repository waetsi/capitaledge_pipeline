# CapitalEdge Analytics Data Pipeline

## Project Overview
This project was developed for the CapitalEdge Analytics capstone project. It automates the extraction, transformation, and loading of financial stock data using Python.

## Objectives
- Automate financial data collection from an API
- Store raw data in JSON format
- Transform raw JSON into structured tabular data
- Implement incremental loading to avoid duplicate records
- Execute the pipeline automatically through a main script

## Project Workflow
1. Extract financial stock data from Alpha Vantage API
2. Store raw data in the `data/raw/` folder
3. Transform the JSON data into a cleaned pandas DataFrame
4. Save processed data into `data/processed/stock_data.csv`
5. Append only new records using incremental loading
6. Run the full pipeline through `main.py`

## Project Structure
```text
capitaledge_pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── main.py
├── notebooks/
│   ├── extract.ipynb
│   └── transform.ipynb
├── README.md
└── requirements.txt
Technologies Used
Python
Pandas
Requests
Jupyter Notebook
Alpha Vantage API
How to Run

Activate your virtual environment, then run: python scripts/main.py
Key Features
Automated API extraction
Raw data storage
Data transformation and cleaning
Incremental loading
End-to-end pipeline execution
Business Value

This solution reduces manual effort, improves data consistency, minimizes duplication, and supports scalable financial data processing.

Author

WAETSI Anyanwu