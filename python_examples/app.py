"""
We need to create list of functions with growing addition
"""


def func(x):
    return x + 0


def func1(x):
    return x + 1


def func2(x):
    return x + 2


def func3(x):
    return x + 3


data_manual = [func, func1, func2, func3]

# data = [lambda x: x + i for i in range(4)]
data = [lambda x, y=i: x + y for i in range(4)]

print(data[0])
print(data_manual[0])

for func in data:
    print(func(10))
