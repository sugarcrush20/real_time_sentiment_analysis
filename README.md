# Real-Time Twitter Sentiment Analysis with Kafka, Spark, MongoDB, and Django

## 🔍 Project Summary

This project demonstrates a real-time sentiment analysis system built around Twitter data. It brings together powerful tools in the big data ecosystem to ingest, process, analyze, store, and visualize sentiment-related insights from tweets in real time.

## 🛠️ Technology Stack

- **Apache Kafka** – Real-time data ingestion from a Twitter dataset  
- **Apache Spark Streaming (MLlib)** – Stream processing and sentiment classification  
- **MongoDB** – Persistent storage for processed data  
- **Django** – Web framework for dashboard visualization  
- **Chart.js & Matplotlib** – For plotting data on the dashboard  

![Project Architecture](imgs/flow.png)

## ✨ Key Features

- **Live Tweet Ingestion**: Stream tweets using Kafka from a dataset  
- **Stream Processing & Sentiment Analysis**: Spark Streaming performs real-time classification into positive, negative, or neutral sentiments  
- **Data Storage**: MongoDB stores the analysis results  
- **Interactive Dashboard**: Django-powered dashboard to explore data trends and view tweet classifications visually  

## 📊 Dataset Information

The project uses two datasets: `twitter_training.csv` and `twitter_validation.csv`. These datasets are used to train and validate the sentiment classification model.

Each record includes:
- Tweet ID (int)
- Entity (string)
- Sentiment (Target: string)
- Tweet Content (string)

Dataset Source: [Kaggle – Twitter Entity Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)

## 📁 Project Directory Structure

```
├── Django-Dashboard/         # Django web app for dashboard
├── Kafka-PySpark/           # Kafka producer and Spark streaming consumer
├── ML PySpark Model/        # Model training notebooks and datasets
├── zk-single-kafka-single.yml  # Docker config for Kafka
├── bigdataproject rapport/  # Report (French)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- Docker (for Kafka)  
- Apache Kafka  
- Apache Spark (with PySpark)  
- MongoDB  
- Django  

### 1. Clone the Repository

```bash
git clone https://github.com/drisskhattabi6/Real-Time-Twitter-Sentiment-Analysis.git
cd Real-Time-Twitter-Sentiment-Analysis
```

### 2. Install Docker Desktop

Follow [Docker Docs](https://docs.docker.com/get-docker/) to install Docker.

### 3. Set Up Kafka using Docker Compose

```bash
docker-compose -f zk-single-kafka-single.yml up -d
```

### 4. Start MongoDB

Start MongoDB manually or using services.

```bash
sudo systemctl start mongod
```

Optional: Use **MongoDB Compass** to visually manage your database.

### 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 🧠 Running the Pipeline

### Kafka and Spark Streaming

1. Navigate to the Kafka-Spark app:

```bash
cd Kafka-PySpark
```

2. Start Kafka Producer Shell (via Docker or terminal):

```bash
docker exec -it <kafka-container-id> /bin/bash
```

3. Create Kafka Topic:

```bash
kafka-topics --create --topic twitter --bootstrap-server localhost:9092
```

4. Run the Kafka Producer:

```bash
python producer-validation-tweets.py
```

5. Run Spark Streaming Consumer:

```bash
python consumer-pyspark.py
```

> After successful processing, MongoDB will display results like this:  
![MongoDB Compass Screenshot](imgs/img4.png)

## 🌐 Django Dashboard

1. Navigate to the Django app:

```bash
cd Django-Dashboard
```

2. Collect Static Files:

```bash
python manage.py collectstatic
```

3. Run Django Server:

```bash
python manage.py runserver
```

4. Access the dashboard:  
Open your browser and go to: `http://127.0.0.1:8000`

![Dashboard Screenshot](imgs/img2.png)  
![Live View](imgs/img3.png)

## 💡 Additional Notes

- The dashboard fetches real-time data from MongoDB.  
- Users can classify custom text at: `http://127.0.0.1:8000/classify`  
- Includes tables and plots: sentiment distribution, bar charts, and pie charts.



