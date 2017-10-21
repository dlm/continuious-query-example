import sys

from query_runner import QueryRunner

min_ever = float('inf')

def query(new_val):
    global min_ever
    if new_val < min_ever:
        min_ever = new_val
        print('I got a new val %d' % min_ever)

QueryRunner.run(query)
