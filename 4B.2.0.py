
def beforeExam(d, sumTime, minTime, maxTime):
    if sumTime < sum(minTime) or sumTime > sum(maxTime):
        print("NO")
    else:
        print("YES")
        li = []
        for i in range(d):
            li.append(minTime[i])
        sumTime = sumTime - sum(minTime)

        j = 0
        while sumTime != 0:
            if sumTime >= maxTime[j] - minTime[j]:
                li[j] = maxTime[j]
                sumTime = sumTime - (maxTime[j] - minTime[j])
            else:
                li[j] = li[j] + sumTime
                sumTime = 0
            j += 1
        print(*li)  # * operator is used to print list separated by space

d, sumTime = [int(x) for x in input().split()]
minTime = []
maxTime = []
for i in range(d):
    minMax = input().split()
    minTime.append(int(minMax[0]))
    maxTime.append(int(minMax[1]))

beforeExam(d, sumTime, minTime, maxTime)