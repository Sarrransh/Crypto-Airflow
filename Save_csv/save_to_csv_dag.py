from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
import csv
from datetime import datetime

default_args = {
    'owner': 'prathmesh',
    'retries': 2,
}


with DAG(
    dag_id='mysql_to_csv',
    default_args=default_args,
    description='Fetch data from MySQL and store it in a CSV file',
    start_date=datetime(2024, 9, 9),
    schedule_interval='@daily'
) as dag:

    def fetch_data_from_mysql():
        mysql_hook = MySqlHook(mysql_conn_id='mysql-conn') 
        connection = mysql_hook.get_conn()
        cursor = connection.cursor()
        query = "SELECT * FROM crypto_data"  
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]  
        cursor.close()
        connection.close()
        return columns, rows
    
    def save_to_csv(**context):
        columns, rows = context['task_instance'].xcom_pull(task_ids='fetch_data_from_mysql')
        file_path = '/opt/airflow/data/crypto_data.csv'  
        
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(columns)  
            writer.writerows(rows)    


    fetch_task = PythonOperator(
        task_id='fetch_data_from_mysql',
        python_callable=fetch_data_from_mysql
    )

    save_task = PythonOperator(
        task_id='save_to_csv',
        python_callable=save_to_csv,
        provide_context=True 
    )

   
    fetch_task >> save_task
