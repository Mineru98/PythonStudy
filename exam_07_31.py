def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


for i in range(2, 9 + 1):
    for j in range(1, 9 + 1):
        print("{} x {} = {}".format(i, j, mul(i, j)))