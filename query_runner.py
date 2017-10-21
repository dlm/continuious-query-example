import rabbit

class QueryRunner(object):

    @classmethod
    def run(cls, user_method):
        (connection, channel, _, exchange_name) = rabbit.RabbitConnection.setup()

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=exchange_name, queue=queue_name)

        print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            user_method(int(body))

        channel.basic_consume(callback, queue=queue_name, no_ack=True)

        channel.start_consuming()
