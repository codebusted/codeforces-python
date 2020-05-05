
# the problem with this solution is it won't consider the minTime
# it focuses on studying maxTime hrs each day till the sumTime becomes zero
# this means completing work as soon as possible

def beforeExam(d, sumTime, minTime, maxTime):
    if sumTime < minTime[0] or sumTime > sum(maxTime):
        print("NO")
    else:
        print("YES")
        li = []
        for i in range(d):
            if sumTime > maxTime[i]:
                li.append(maxTime[i])
                sumTime = sumTime - maxTime[i]
            elif sumTime < maxTime[i]:
                li.append(sumTime)
                sumTime = 0
            else:
                li.append(sumTime)
                sumTime = 0
        print(*li)  # * operator is used to print list separated by space

d, sumTime = [int(x) for x in input().split()]
minTime = []
maxTime = []
for i in range(d):
    minMax = input().split()
    minTime.append(int(minMax[0]))
    maxTime.append(int(minMax[1]))

beforeExam(d, sumTime, minTime, maxTime)