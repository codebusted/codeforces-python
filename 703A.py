
n = int(input())
mishka = 0
chris = 0
for i in range(n):
    mc = input().split()
    m = mc[0]
    c = mc[1]
    if m > c:
        mishka += 1
    elif m < c:
        chris += 1
    else:
        pass

if mishka > chris:
    print('Mishka')
elif mishka < chris:
    print('Chris')
else:
    print('Friendship is magic!^^')