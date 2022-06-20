mas = []
mas += bin(int(input()))
mas.pop(1)
mas = list(map(int, mas))
print(sum(mas))
