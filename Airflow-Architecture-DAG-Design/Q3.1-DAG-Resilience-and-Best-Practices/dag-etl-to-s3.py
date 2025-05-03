from airflow import DAG
from airflow.decorators import task, task_group
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

import requests
import json
from datetime import timedelta

# Constants
API_URL = "https://api.lab.io/data"
S3_BUCKET = "s3-bucket-name"
S3_KEY = "etl/output.json"

default_args = {
    "retries": 3,
    "retry_delay": timedelta(seconds=30),
    "retry_exponential_backoff": True,
    "max_retry_delay": timedelta(minutes=10)
}

with DAG(
    dag_id="api_to_s3_etl",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    tags=["etl", "api", "s3"],
) as dag:

    @task
    def extract():
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    @task
    def transform(data: dict):
        # Minimal transformation: Filter keys
        transformed = [{"id": item["id"], "value": item["value"]} for item in data["results"]]
        return transformed

    @task
    def load_to_s3(data: list):
        s3 = S3Hook(aws_conn_id="aws_default")
        json_data = json.dumps(data)
        s3.load_string(
            string_data=json_data,
            key=S3_KEY,
            bucket_name=S3_BUCKET,
            replace=True
        )

    @task_group(group_id="etl_pipeline")
    def etl_group():
        raw_data = extract()
        transformed_data = transform(raw_data)
        load_to_s3(transformed_data)

    etl_group()
