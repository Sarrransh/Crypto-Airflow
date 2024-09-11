from airflow.providers.mysql.hooks.mysql import MySqlHook

def store_data_in_mysql(**context):
    data = context['task_instance'].xcom_pull(task_ids='transform_data')
    mysql_hook = MySqlHook(mysql_conn_id='mysql-conn')  
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_data (
            id VARCHAR(50) PRIMARY KEY,
            symbol VARCHAR(10),
            name VARCHAR(100),
            current_price FLOAT,
            market_cap BIGINT,
            total_volume BIGINT
        );
    ''')


    for row in data:
        cursor.execute('''
            INSERT INTO crypto_data (id, symbol, name, current_price, market_cap, total_volume)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            current_price = VALUES(current_price),
            market_cap = VALUES(market_cap),
            total_volume = VALUES(total_volume);
        ''', (row['id'], row['symbol'], row['name'], row['current_price'], row['market_cap'], row['total_volume']))

    connection.commit()
    cursor.close()