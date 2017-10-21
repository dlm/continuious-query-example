import sys

from query_runner import QueryRunner

max_ever = -float('inf')

def query(new_val):
    global max_ever
    if new_val > max_ever:
        max_ever = new_val
        print('I got a new val %d' % max_ever)

QueryRunner.run(query)
