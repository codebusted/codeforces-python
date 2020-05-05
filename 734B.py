def digits(k):
    x = min(k[0], k[2], k[3])
    y = min(k[1], k[0] - x)
    return (256 * x + 32 * y)

k_li = input().split()
k = []
for i in range(len(k_li)):
    k.append(int(k_li[i]))

res = digits(k)
print(res)