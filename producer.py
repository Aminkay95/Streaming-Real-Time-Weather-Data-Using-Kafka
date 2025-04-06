from confluent_kafka import Producer
from main import extract_data, transform_data, load_data_to_db
import time
import json
config = {
    'bootstrap.servers' : 'localhost:9092',
    'client.id':'python-producer'
}

producer = Producer(config)
topic = 'weather_topic'

def delivery_report(err, msg):
    if err is not None:
        print(f'Delivery failed: {err}')
    else:
        print(f'Delivered to {msg.topic()}[{msg.partition()}]')

while True:

    #extract data from the api
    data = extract_data()
    # transform the data
    transformed_data = transform_data(data)
    
    # looping through the data and writing into the topic weather_data
    for record in transformed_data:
        producer.produce(topic, value = json.dumps(record), callback = delivery_report )
        producer.poll(0)
    
    time.sleep(600)


