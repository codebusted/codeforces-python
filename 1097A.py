
def cardGame(inHand, onTable):
    for i in range(5):
        eachCard = onTable[i]
        if inHand[0] == eachCard[0] or inHand[1] == eachCard[1]:
            return "YES" 
    return 'NO'

inHand = list(input())
onTable = input().split()

result = cardGame(inHand, onTable)
print(result)