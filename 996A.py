
def theLottery(n):
    bills = 0
    if n >= 100:
        while n >= 100:
            n = n - 100
            bills += 1
    if n in range(20, 100):
        while n >= 20:
            n = n - 20
            bills += 1
    if n in range(10, 20):
        while n >= 10:
            n = n - 10
            bills += 1
    if n in range(5, 10):
        n = n - 5
        bills += 1
    if n in range(1, 5):
        while n >= 1:
            n = n - 1
            bills += 1
    return bills

n = int(input())

result = theLottery(n)
print(result)