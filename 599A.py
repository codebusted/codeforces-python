ans = list(map(int, input().split()))
print(min(ans[0]+ans[0]+ans[1]+ans[1], ans[0]+ans[2]+ans[1], ans[0]+ans[2]+ans[2]+ans[0], ans[1]+ans[2]+ans[2]+ans[1]))
