
def theLottery(n):
    bills = 0
    if n >= 100:
        q, n = divmod(n, 100)
        bills = bills + q
    if n >= 20:
        q, n = divmod(n, 20)
        bills = bills + q
    if n >= 10:
        q, n = divmod(n, 10)
        bills = bills + q
    if n >= 5:
        q, n = divmod(n, 5)
        bills = bills + q
    if n >= 1:
        q, n = divmod(n, 1)
        bills = bills + q
    return bills

n = int(input())

result = theLottery(n)
print(result)