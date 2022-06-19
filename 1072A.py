tmp = list(map(int, input().split()))
w, h, k = tmp[0], tmp[1], tmp[2]
ans = 0
for _ in range(k):
	ans += 2 * (w - 1) + 2 * (h - 1)
	w -= 4
	h -= 4
print(ans)
