# CapitalEdge Analytics Data Pipeline

## 📌 Project Overview
This project demonstrates an end-to-end data pipeline that automates the extraction, transformation, and orchestration of financial stock data using Python and Apache Airflow.

---

## 🗂️ Project Structure
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
├── airflow_dag/
│   └── capitaledge_pipeline_dag.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt



## Technologies Used
Python
Pandas
Apache Airflow
WSL (Ubuntu)
Azure Blob Storage (optional)
Alpha Vantage API
---

## 🎯 Objectives
- Automate financial data collection from Alpha Vantage API  
- Store raw data in JSON format  
- Transform raw JSON into structured tabular data  
- Implement incremental loading to avoid duplicate records  
- Orchestrate the pipeline using Apache Airflow  

---

## 🔄 Pipeline Architecture

```text
Raw JSON → Extract → Transform → Processed CSV → (Azure Storage)
                      ↑
                 Airflow DAG

## HOW TO RUN
    1. Clone the repository
      git clone https://github.com/waetsi/capitaledge_pipeline
      cd capitaledge_pipeline

    2. Install Dependencies
    pip install -r requirements.txt

    3. Set environment variables

        Create a .env file: ALPHAVANTAGE_API_KEY=your_api_key_here
        AZURE_STORAGE_CONNECTION_STRING=your_connection_string

    4. Run pipeline manually
        python scripts/main.py

    5. Run with Airflow
        airflow standalone

    Then open: http://localhost:8080

## Key Features
Automated API extraction
Data cleaning and transformation
Incremental data loading
Airflow orchestration
Error handling and debugging
Optional Azure cloud storage

## Output

The pipeline generates a structured dataset:

Cleaned stock data
Calculated metrics
Ready for analytics or visualization


## Business Value

This solution:

Reduces manual data processing
Improves data accuracy and consistency
Enables scalable data workflows
Demonstrates real-world data engineering practices


## Challenges & Solutions
Airflow setup in WSL → resolved with standalone mode
Dependency issues → resolved using virtual environments
File path errors → fixed using correct working directory
API rate limits → managed with controlled request delays


## Future Improvements
Real-time data ingestion
Integration with cloud databases
Dashboard visualization (Power BI / Tableau)
Scheduling and monitoring enhancements



## Author

WAETSI Anyanwu



