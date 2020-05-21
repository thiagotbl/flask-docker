import pika

class Consumer(object):
    def start(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbit', port=5672, credentials=credentials
            )
        )
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_consume(
            queue='hello',
            on_message_callback=self.callback,
            auto_ack=True
        )

        channel.start_consuming()

    def callback(self, _ch, _method, _properties, body):
        print("Received %r" % body)
