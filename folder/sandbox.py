"""
Some information
"""
import time
from random import randint, choice

colors = ["red","black","yellow","white"]


def something(init_count = 0 ):
    while True:
        response_value = randint(1, 3)
        if response_value == 3:
            yield "not ready"
        if response_value == 2:
            yield choice(colors)
        else:
            yield "Empty response"



connection = something()

data = []
for i in range(10):
    data.append(next(connection))

    print(data)


