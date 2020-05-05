# vasya the hipster
import math

def sockPair(a, b):
    diffsock = min(a, b)
    samesock = math.floor(abs(a - b) / 2)
    return diffsock, samesock

ab = input().split()
a = int(ab[0])
b = int(ab[1])

diffsock, samesock =sockPair(a, b)
print(diffsock, samesock)