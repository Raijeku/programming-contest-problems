from datetime import datetime

start = datetime.now()

def getPosition(marbles, queries): 
    marblesCopy = marbles.copy()
    queriesCopy = queries.copy()
    positionArray = [None] * len(queriesCopy)
    marbleArray = [None] * len(queriesCopy)
    amountInvalid = 0
    previousMin = -1
    position = 0
    for index in range(len(marblesCopy)):
        min=10001
        minIndex = -1
        for marbleIndex in range(len(marblesCopy)):
            if previousMin == marblesCopy[marbleIndex] and previousMin != 10001:
                if amountInvalid == 1:
                    position -= 1
                marblesCopy[marbleIndex] = 10001
                amountInvalid = 1
            if marblesCopy[marbleIndex] < min and previousMin != 10001:
                min = marblesCopy[marbleIndex]
                minIndex = marbleIndex

        amountInvalid = 0
        previousMin = min
        position += 1 
        if previousMin != 10001:
            for queryIndex in range(len(queriesCopy)):
                if min == queriesCopy[queryIndex]:
                    positionArray[queryIndex] = position
                    queriesCopy[queryIndex] = 10001
    
    return positionArray

setting = input()
settingArray = setting.split(' ')
N = int(settingArray[0])
Q = int(settingArray[1])
case = 0

while not (N == 0 and Q == 0):
    case = case + 1
    marbles = []
    queries = []
    for i in range(N):
        marbles.append(int(input()))
    for i in range(Q):
        queries.append(int(input()))
    #marbles.sort()
    print("CASE# " + str(case) + ":")
    foundPositions = getPosition(marbles, queries)
    for positionIndex in range(len(foundPositions)):
        if foundPositions[positionIndex] != None:
            print(str(queries[positionIndex]) + " found at " + str(foundPositions[positionIndex]))
        else:
            print(str(queries[positionIndex]) + " not found")
    setting = input()
    settingArray = setting.split(' ')
    N = int(settingArray[0])
    Q = int(settingArray[1])

total = datetime.now()-start
print(total.total_seconds() * 1000)