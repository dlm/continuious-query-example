import pika

class RabbitConnection(object):

    @classmethod
    def setup(cls):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        return (connection, channel)



