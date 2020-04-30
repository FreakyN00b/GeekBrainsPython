from itertools import count
from math import factorial


def my_gen():
    for el in count(1):
        yield factorial(el)


gen = my_gen()
x = 0
for i in gen:
    if x <= 15:
        print(f"Factorial {x} = {i}")
        x += 1
    else:
        break
