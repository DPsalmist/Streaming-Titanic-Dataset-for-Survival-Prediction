# Import necessary libraries
import pandas as pd
from confluent_kafka import Producer, Consumer, KafkaError
import seaborn as sns
import json
import time

# Read data
file = '/Users/damilare/Documents/JBassey/distributed system/datasets/titanic.csv'
data = pd.read_csv(file)
data.head()

# Download Titanic Dataset
def load_titanic_data(filepath=file):
    return pd.read_csv(filepath)


# Kafka Producer to simulate data streaming
def produce_data(data, topic):
    producer = Producer({'bootstrap.servers': 'localhost:9092'})
    for index, row in data.iterrows():
        # Convert row to JSON
        message = row.to_json()
        producer.produce(topic, key=str(index), value=message)
        producer.flush()
        time.sleep(0.5)  # Simulate delay between records
    print("Data streaming completed.")


# Kafka Consumer to read streamed data
def consume_data(topic):
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'titanic_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            # Decode the message and print it
            data = json.loads(msg.value().decode('utf-8'))
            print("Consumed data:", data)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


# Main function
if __name__ == "__main__":
    topic_name = "titanic_data_stream"

    # Load the Titanic dataset
    titanic_data = load_titanic_data()

    # Simulate data streaming
    print("Streaming data...")
    produce_data(titanic_data, topic_name)

    # Consume the data
    print("\nConsuming data...")
    consume_data(topic_name)