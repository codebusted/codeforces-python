n = int(input())
tmp = n
childnum = 1
mas = []
if n in [1, 2]:
	print(1)
	print(n)
	raise SystemExit
while True:
	if n < 0:
		childnum -= 2
		mas.pop()
		mas[-1] += tmp - sum(mas)
		break
	mas.append(childnum)
	n -= childnum
	childnum += 1

print(childnum)
print(*mas)
