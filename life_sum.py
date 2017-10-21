import sys

from query_runner import QueryRunner

life_sum = 0

def query(new_val):
    global life_sum
    life_sum += new_val
    print('New sum %d' % life_sum)

QueryRunner.run(query)
