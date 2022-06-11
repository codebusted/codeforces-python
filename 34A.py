lenmas = int(input())
mas = list(map(int, input().split()))
minn = max(mas[0], mas[-1]) - min(mas[0], mas[-1]) 
flag = False
for i in range(lenmas-1):
	if max(mas[i], mas[i+1]) - min(mas[i], mas [i+1]) < minn:
		minn = max(mas[i], mas[i+1]) - min(mas[i], mas [i+1])
		ans = i
		flag = True
if flag:
	print(ans+1, ans+2)
else:
	print(lenmas, 1)
