from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


#Importing the functions from different files
from crypto_data_fetch import  fetch_crypto_data
from crypto_data_transform import transform_data
from store_in_mysql import store_data_in_mysql


default_args = {
    'owner': '',
    'retries': 2,
}

with DAG(
    dag_id='crypto_data_pipeline_v2',
    default_args=default_args,
    description='Fetch, transform, and store cryptocurrency market data into MySQL',
    start_date=datetime(2024, 9, 9),
    schedule_interval='@daily'
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_crypto_data',
        python_callable=fetch_crypto_data
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True  # This passes data between tasks
    )

    store_task = PythonOperator(
        task_id='store_data_in_mysql',
        python_callable=store_data_in_mysql,
        provide_context=True
    )

    fetch_task >> transform_task >> store_task
