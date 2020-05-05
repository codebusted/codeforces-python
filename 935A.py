
def fafaAndCompany(n):
    l = 1
    ways = 0
    for _ in range(n):
        if (n - l) != 0 and (n - l) % l == 0:
            ways += 1
        l += 1
    return ways

n = int(input())

result = fafaAndCompany(n)
print(result)