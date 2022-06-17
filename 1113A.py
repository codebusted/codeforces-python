tmp = list(map(int, input().split()))
n = tmp[0]
v = tmp[1]
ans = v - 1
if n<=v:
    print(n-1)  
else:
    for i in range(n - v + 1):
    ans += i
    print(ans)
