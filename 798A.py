pal = input()
revpal = pal [::-1]
difcount = 0
for i in range(len(pal)):
	if pal[i] != revpal[i]:
		difcount +=1
if difcount == 2 or (difcount == 0 and len(pal) % 2 == 1):
	print('YES')
else:
	print('NO')
