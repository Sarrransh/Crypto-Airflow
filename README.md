# Airflow Crypto Data Pipeline Project

This repository contains an **Apache Airflow** project that performs two main actions:

1. **Fetch, Transform, and Load (ETL) Cryptocurrency Data**:  
   A DAG that fetches cryptocurrency data from a public API, transforms it, and loads it into a MySQL database hosted on Aiven.

2. **Save Data to CSV**:  
   A DAG that retrieves the cryptocurrency data from the MySQL database and saves it locally in a CSV file.

## Project Overview

This project demonstrates a simple use of **Apache Airflow** for orchestrating data workflows. It showcases how to:

- **Fetch data** using an API.
- **Transform data** by processing and extracting relevant fields.
- **Store data** in a **MySQL database**.
- **Retrieve data** and save it locally as a CSV file.

### DAG 1: ETL Cryptocurrency Data
The first DAG performs the following steps:
1. **Fetch Data**: Uses the [CoinGecko API](https://www.coingecko.com/en/api) to retrieve market data of the top 100 cryptocurrencies.
2. **Transform Data**: Selects relevant fields like `id`, `symbol`, `name`, `current_price`, `market_cap`, and `total_volume` from the API response.
3. **Load Data**: Stores the transformed data in a MySQL database hosted on Aiven.

### DAG 2: Save Data to CSV
The second DAG:
1. **Connects to the MySQL database**: Queries the database for the stored cryptocurrency data.
2. **Saves Data Locally**: Writes the retrieved data to a CSV file and stores it in the local directory.

## Setup Instructions

### Prerequisites
- **Docker**
- **Aiven** MySQL Database
- **Apache Airflow**



## Bash Commands Used

1. **Run Docker Compose**:
   ```
   docker-compose up -d
   ```
   - **Explanation**: This command starts the Airflow services using Docker Compose in detached mode (running in the background).

2. **List running Docker containers**:
   ```
   docker ps
   ```
   - **Explanation**: This command lists all the running Docker containers, including Airflow web server and scheduler.

3. **Access the running Airflow container**:
   ```
   docker exec -it <container_name> /bin/bash
   ```
   - **Explanation**: Replace `<container_name>` with the name of your Airflow web server container (you can find it using the `docker ps` command). This gives you shell access to the running container.

4. **Copy a file from the container to your local machine**:
   ```
   docker cp airflow-docker-airflow-webserver-1:/opt/airflow/crypto_data.csv /path/to/local/folder/
   ```
   - **Explanation**: This command copies the CSV file from the Airflow container to your local machine. Replace `/path/to/local/folder/` with the actual path where you want to save the file locally.

5. **Stop and remove all containers**:
   ```
   docker-compose down
   ```
   - **Explanation**: Stops and removes the containers, networks, and volumes used by the services defined in `docker-compose.yml`.

6. **View logs for specific DAG runs**:
   ```
   docker logs <container_name>
   ```
   - **Explanation**: This command allows you to view the logs of a specific container to troubleshoot DAG runs. Replace `<container_name>` with the name of the Airflow web server or scheduler container.

## Getting Started

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/yourprojectname.git
   ```

2. **Set up Airflow environment**:
   - Ensure you have Docker and Docker Compose installed on your machine.
   - Start the Airflow services:
     ```
     docker-compose up -d
     ```

3. **Configure MySQL connection**:
   - Set up a MySQL database on Aiven (or another hosting platform) and configure the connection details in Airflow.

4. **Run the DAGs**:
   - Access the Airflow web UI at `http://localhost:8080` and trigger the DAGs to run the ETL process.

5. **Copy CSV to local machine**:
   - Once the `save_to_csv_dag` has run, copy the CSV file from the Airflow container to your local machine using:
     ```
     docker cp airflow-docker-airflow-webserver-1:/opt/airflow/data/crypto_data.csv /path/to/local/folder/
     ```


### Folder Structure
```
.
.
├── dags/
│   ├── crypto_data_etl.py          # Main DAG for crypto ETL pipeline
│   ├── crypto_data_fetch.py        # Fetch cryptocurrency data from API
│   ├── crypto_data_transform.py    # Transform the fetched data
│   ├── store_in_mysql.py           # Store transformed data into MySQL
│   ├── save_to_csv_dag.py          # Save data to CSV DAG
├── logs/                           # Airflow logs
├── config/                         # Configuration files
└── docker-compose.yml              # Docker setup for Airflow and services

```

## API Used

- [CoinGecko API](https://www.coingecko.com/en/api): Fetches cryptocurrency market data.

- The Api in use does not require an API Key

**API Endpoint:**
```
https://api.coingecko.com/api/v3/coins/markets
```

**Parameters used:**
- `vs_currency=usd`: Fetches data in USD.
- `order=market_cap_desc`: Orders the data by market capitalization in descending order.
- `per_page=100`: Limits the result to 100 cryptocurrencies per page.
- `page=1`: Fetches the first page of results.

This API provides data on cryptocurrency markets, including prices, market caps, and volumes, and is public and free to use without an API key.

## Technologies Used

- **Apache Airflow**: For workflow orchestration.
- **MySQL**: Database for storing cryptocurrency data.
- **Docker**: For containerization and managing Airflow services.
- **Aiven**: Managed MySQL database hosting.

## Future Enhancements

- Add data validation and error handling for failed API requests.
- Implement data partitioning to optimize database queries.

---

This README gives an overview of your project, instructions for setup, and a description of the workflow. Feel free to customize it further to fit your project’s specific details!
