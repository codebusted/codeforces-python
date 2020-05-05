
def bigBear(a, b):
    i = 0
    while a <= b:
        a = a * 3
        b = b * 2
        i += 1
    return i

ab = input().split()
a = int(ab[0])
b = int(ab[1])

result = bigBear(a, b)
print(result)