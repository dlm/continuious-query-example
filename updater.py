import rabbit

(connection, channel) = rabbit.RabbitConnection.setup()

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='key:val')
print(" [x] Sent 'Hello World!'")

connection.close()
