import requests

def fetch_crypto_data(**context):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1'
    response = requests.get(url)
    data = response.json()
    context['task_instance'].xcom_push(key='crypto_data', value=data)