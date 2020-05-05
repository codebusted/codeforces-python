
def fractionOrangeJuice(n, p):
    li = []
    for i in range(n):
        li.append(int(p[i]))
    total = sum(li)
    return total / n

n = int(input())
p = input().split()
result = fractionOrangeJuice(n, p)
print(result)