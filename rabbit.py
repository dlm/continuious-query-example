import pika

class RabbitConnection(object):

    @classmethod
    def setup(cls, queue_name='updates', exchange_name='logs'):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        queue_result = channel.queue_declare(queue=queue_name)
        exchange_result = channel.exchange_declare(exchange=exchange_name,
                                                   exchange_type='fanout')
        return (connection, channel, queue_name, exchange_name)

