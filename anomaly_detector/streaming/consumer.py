# This file is not being used currently, it's purpose is to give a brief idea of how this would be handled in the
# real-world production scenario
from pyspark.sql import SparkSession
from pyspark.sql.connect.functions import from_json
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StringType, TimestampType, ArrayType, LongType, DecimalType, StructField

spark = SparkSession.builder.appName('Anomaly Detection').getOrCreate()

# consumer = KafkaConsumer('anomaly_detection_topic', bootstrap_servers=['localhost:9092'],
#                          group_id='anomaly_detection_group')

# Schema definition for our data
schema = StructType([
    StructField('resource', LongType(), True),
    StructField('type', StringType(), True),
    StructField('resource_attributes', StringType(), True),
    StructField('ts', TimestampType(), True),
    StructField('values', ArrayType(DecimalType()), True)
])

# Spark dataframe that consumes our Kafka stream
df = spark.readStream.format('kafka') \
    .option('kafka.bootstrap.servers', 'localhost:9092') \
    .option('subscribe', 'anomaly_detection_topic') \
    .load() \
    .select(from_json(col('value').cast('string'), schema).alias('data')) \
    .select('data.*')

# Split the data into separate streams for each resource
resource_streams = df.groupBy('resource')

# Now the processing of individual streams can happen here
