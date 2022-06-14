tax = -list(map(int, input().split()))[1]
prices = list(map(int, input().split()))
prices.sort()
m = int(input())
ans = 0
if m > len(prices):
	m -= len(prices)
	ans += sum(prices)
	ans += m * tax
else:
	for i in range(m):
		ans += prices[i]
print(ans)
