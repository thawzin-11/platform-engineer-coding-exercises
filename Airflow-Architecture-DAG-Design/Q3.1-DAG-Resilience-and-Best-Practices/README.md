Task: Write a minimal Airflow DAG that:

    - Extracts data from an API, transforms it, and stores it into S3.
    - Has clear task separation using appropriate operators.
    - Retries with exponential backoff on failure.
    - Uses task_group or @task decorator to group logic if needed.

Focus: DAG composition, operators, retries, structure, Airflow best practices.

-------------

Solution:

- Make sure you have the following Airflow providers installed:

    pip install apache-airflow-providers-amazon


Note:

- @task_group: Logically groups ETL tasks for readability.

- @task decorators: Lightweight and readable function-based tasks.

- default_args: Implements exponential backoff and retry behavior.

- S3Hook: Uses Airflow’s AWS abstraction layer (configure aws_default connection in UI or via environment).