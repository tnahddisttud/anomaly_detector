# This file is not being used currently, but this is how we'd mimic real-world scenario where logs are streamed
# one-by-one. This stream will be subscribed by our consumer for anomaly detection
import csv
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

with open('anomaly_detector/resources/metrics_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Send each row as a message to Kafka
        producer.send('anomaly_detection_topic', value=row)
