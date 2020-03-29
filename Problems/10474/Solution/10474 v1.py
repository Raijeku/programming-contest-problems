def getPosition(marbles, query): 
    marblesCopy = marbles.copy()
    position = 0
    for index in range(len(marblesCopy)):
        min=10000
        minIndex = -1
        for marbleIndex in range(len(marblesCopy)):
            if marblesCopy[marbleIndex] <= min:
                min = marblesCopy[marbleIndex]
                minIndex = marbleIndex
        position += 1
        if query != min:
            marblesCopy.pop(minIndex)
            index -= 1
        else: 
            break

    return position

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
    for query in queries:
        if not query in marbles:
            print(str(query) + " not found")
        else:
            print(str(query) + " found at " + str(getPosition(marbles, query)))
    setting = input()
    settingArray = setting.split(' ')
    N = int(settingArray[0])
    Q = int(settingArray[1])
