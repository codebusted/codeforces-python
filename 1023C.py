for _ in range(int(input())):
	seq = input()
	countab = 0
	countbc = 0
	countac = 0
	counta = 0
	countb = 0
	countc = 0
	ans = [True, True, True, True, True, True]
	for i in range(len(seq)):
		if seq[i] == 'A':
			countab += 1
			countbc -= 1
			countac += 1
			counta += 1
			countb -= 1
			countc -= 1
		elif seq[i] == 'B':
			countab += 1
			countbc += 1
			countac -= 1
			counta -= 1
			countb += 1
			countc -= 1
		elif seq[i] == 'C':
			countab -= 1
			countbc += 1
			countac += 1
			counta -= 1
			countb -= 1
			countc += 1
		if countab < 0:
			ans[0] = False
		if countbc < 0:
			ans[1] = False
		if countac < 0:
			ans[2] = False
		if counta < 0:
			ans[3] = False
		if countb < 0:
			ans[4] = False
		if countc < 0:
			ans[5] = False
	if countab != 0:
		ans[0] = False
	if countbc != 0:
		ans[1] = False
	if countac != 0:
		ans[2] = False
	if counta != 0:
		ans[3] = False
	if countb != 0:
		ans[4] = False
	if countc != 0:
		ans[5] = False
	if True in ans:
		print('YES')
	else:
		print('NO')
