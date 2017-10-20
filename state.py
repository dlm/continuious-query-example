import rabbit

(connection, channel) = rabbit.RabbitConnection.setup()

state = dict()

def callback(ch, method, properties, body):
    [key, val] = str(body).split(':')
    print(" [x] Received %s %s" % (key, val))
    state[key] = val

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
