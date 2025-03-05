# Streaming-Titanic-Dataset-for-Survival-Prediction

*Objective:*

To establish a data streaming architecture that ingests the Titanic dataset in real-time, simulating a streaming environment for future survival prediction models.

*Features:*

- **Data Ingestion:** Simulates real-time streaming of the Titanic dataset using a Kafka Producer.
- **Data Consumption:** Utilizes a Kafka Consumer to read and display streamed data.
- **Data Visualization:** Provides mechanisms to visualize ingested data for analysis.

*Usage:*

1. **Download the Titanic Dataset:**

    - Obtain the dataset from Kaggle or download it from the repo and save it as titanic.csv.

2. **Set Up the Kafka Environment:**
   - docker-compose up -d


3. **Install necessary dependencies:**
     - pip install pandas confluent_kafka json

5. **Execute the consumer script or notebook to read and display streamed data:**
   - python kafka_consumer.py
   - run Data-Streaming.ipynb in jupyter
