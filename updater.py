import rabbit

import sys

message = sys.argv[1] + ':' + sys.argv[2]

(connection, channel, queue_name, _) = rabbit.RabbitConnection.setup()

channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message)
print(" [x] Sent '%d'", message)

connection.close()
