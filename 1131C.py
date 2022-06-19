junk = input()
mas = list(map(int, input().split()))
mas.sort()
newmas = []
for _ in range(len(mas)):
	newmas.append(0)
for i in range(len(mas)):
	idee = newmas.index(0)
	newmas[idee]=mas[i]
	newmas.reverse()
print(*newmas)
