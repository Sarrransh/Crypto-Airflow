def transform_data(**context):
    raw_data = context['task_instance'].xcom_pull(task_ids='fetch_crypto_data', key='crypto_data')
    transformed_data = []
    for coin in raw_data:
        transformed_data.append({
            'id': coin['id'],
            'symbol': coin['symbol'],
            'name': coin['name'],
            'current_price': round(coin['current_price'], 2),
            'market_cap': coin['market_cap'],
            'total_volume': coin['total_volume']
        })
    return transformed_data