
def antonAndDanik(n, s):
    a = 0
    d = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
        else:
            d += 1
    if a > d:
        print('Anton')
    elif a < d:
        print('Danik')
    else:
        print('Friendship')

n = int(input())
s = list(input())  # list function is used to convert a string to list

antonAndDanik(n, s)