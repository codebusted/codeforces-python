
def easyProblem(n, li):
    for i in range(n):
        if int(li[i]) == 1:
            return "HARD"
    return "EASY"

n = int(input())
li = input().split()

result = easyProblem(n, li)
print(result)