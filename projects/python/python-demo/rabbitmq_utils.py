# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-24 02:57:36 UTC+8
"""

import pika


class RabbitMQConnector:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.credentials = pika.PlainCredentials(username, password)
        self.connection_params = pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials)
        self.connection = None

    def connect(self):
        self.connection = pika.BlockingConnection(self.connection_params)
        return self.connection

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()


class RabbitMQProducer:
    def __init__(self, connector, queue_name):
        self.connector = connector
        self.queue_name = queue_name
        self.channel = self.connector.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)

    def publish(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2  # make message persistent
            )
        )
        print(f" [x] Sent {message}")

    def close(self):
        self.connector.close()


class RabbitMQConsumer:
    def __init__(self, connector, queue_name):
        self.connector = connector
        self.queue_name = queue_name
        self.channel = self.connector.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)

    def consume(self):
        def callback(ch, method, properties, body):
            print(f" [x] Received {body}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


def test_rabbitmq():
    host = 'employ.fairies.ltd'
    port = 51004
    username = 'guest'
    password = 'guest'
    queue_name = 'test_queue'

    # Create a connection
    connector = RabbitMQConnector(host, port, username, password)
    connector.connect()

    # Create a producer and send a message
    producer = RabbitMQProducer(connector, queue_name)
    producer.publish('Hello RabbitMQ!')
    # producer.close()

    # Create a consumer and start consuming messages
    consumer = RabbitMQConsumer(connector, queue_name)
    consumer.consume()
    # consumer.close()


if __name__ == '__main__':
    test_rabbitmq()
