
def wrongSubtraction(n, k):
    for _ in range(k):
        if n % 10 == 0:
            n = n / 10
        else:
            n = n - 1
    return n

nk = input().split()
n = int(nk[0])
k = int(nk[1])

result = wrongSubtraction(n, k)
print(int(result))