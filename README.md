# Fun with RabbitMQ

At systems seminar this week and last, we learned about
[RabbitMQ](https://www.rabbitmq.com/).  This week we did a small hackathon where
we made a very simple continuous query system for a piece of data.

I created two helper classes:
- rabbit.py: which sets up messaging
- query_runner.py: which simplifies writing queries

The reset of the files are programs of the system that should be run.

The system arch is:

```
                                         /- min_ever
|-------|          |-------|            /
|updater|-|queue|->| state |-|exchange|---- max_ever
|-------|          |-------|            \ 
                                         \- life_sum
```

To see all of its glory and splendor:

Run the updater:
```
while true; do sleep 1; python updater.py key $RANDOM; done
```

Run the state:
```
python state.py
```

Run the queries (each in it's own terminal for best effect).
```
python min_ever.py
python max_ever.py
python life_sum.py
```

This is, of course, very basic but it is a good and fun starting point!
