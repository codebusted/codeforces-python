
def hulk(n):
    feeling = "I hate"
    while n != 0:
        n = n - 1
        if n != 0:
            feeling = feeling + " that I love"
            n = n - 1
        if n != 0:
            feeling = feeling + " that I hate"
    feeling = feeling + " it"
    return feeling

n = int(input())

result = hulk(n)
print(result)