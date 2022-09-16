import math

x = float(input("x = "))


def f(_x):
    return ((math.sin(_x) - math.log10(_x)) / math.sqrt(_x * 7)) + math.pow(_x + 4, 2 * x - 8)


print(f(x))
