from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "waetsi",
    "depends_on_past": False,
}

with DAG(
    dag_id="capitaledge_pipeline",
    default_args=default_args,
    description="ETL pipeline for CapitalEdge Analytics",
    schedule_interval="@daily",
    start_date=datetime(2026, 4, 1),
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id="extract_data",
        bash_command='C:/Users/kay2c/Downloads/capitaledge_pipeline/.venv/Scripts/python.exe C:/Users/kay2c/Downloads/capitaledge_pipeline/scripts/extract.py',
    )

    transform_task = BashOperator(
        task_id="transform_data",
        bash_command='C:/Users/kay2c/Downloads/capitaledge_pipeline/.venv/Scripts/python.exe C:/Users/kay2c/Downloads/capitaledge_pipeline/scripts/transform.py',
    )

    load_task = BashOperator(
        task_id="load_to_azure",
        bash_command='C:/Users/kay2c/Downloads/capitaledge_pipeline/.venv/Scripts/python.exe C:/Users/kay2c/Downloads/capitaledge_pipeline/scripts/load.py',
    )

    extract_task >> transform_task >> load_task