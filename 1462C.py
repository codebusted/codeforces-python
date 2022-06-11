def forx(x):
	ans = []
	app = 9
	if x>45:
		print(-1)
		return
	while x >= app and app > 0:
		ans.append(app)
		x -= app
		app -= 1
	if x>0:
		ans.append(x)
	ans.reverse()
	print(*ans, sep = '')
for i in range(int(input())):
	forx(int(input()))
