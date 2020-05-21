import pika
import time
import sys
import threading
from flask import Flask
from consumer import Consumer


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, cruel world!!!'

def start_server():
    print('Starting Flask server')
    app.run(debug=True, host='0.0.0.0')

def start_consumer():
    connect_consumer()

def connect_consumer(retries=0):
    print('Connecting to RabbitMQ server')
    try:
        Consumer().start()
    except pika.exceptions.AMQPConnectionError:
        if retries >= 2:
            raise

        print('Connection error. Retrying in 5 seconds.')
        time.sleep(5)
        connect_consumer(retries + 1)

if __name__ == '__main__':
    threading.Thread(target=start_consumer).start()
    start_server()
