maslen = int(input())
top = []
down = []
for i in range(maslen):
	tmp = list(map(int, input().split()))
	top.append(tmp[0])
	down.append(tmp[1])
if sum(down) % 2 == 0 and sum(top) % 2 == 0:
	print(0)
	raise SystemExit

if (sum(down) % 2 == 0 and sum(top) % 2 != 0) or (sum(down) % 2 != 0 and sum(top) % 2 == 0):
	print(-1)
	raise SystemExit
for i in range(maslen):
	if (top[i] % 2 == 0 and down[i] % 2 != 0) or (top[i] % 2 != 0 and down[i] % 2 == 0):
		print(1)
		raise SystemExit
print(-1)
