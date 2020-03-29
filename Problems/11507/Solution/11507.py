def convertBend(bendString):
    convertedBend = [-1,-1,-1]
    if bendString == "+z":
        convertedBend = [0,0,1]
    elif bendString == "-z":
        convertedBend = [0,0,-1]
    elif bendString == "+y":
        convertedBend = [0,1,0]
    elif bendString == "-y":
        convertedBend = [0,-1,0]
    return convertedBend

def deconvertBend(bendList):
    deconvertedBend = ""
    if bendList == [0,0,1]:
        deconvertedBend = "+z"
    elif bendList == [0,0,-1]:
        deconvertedBend = "-z"
    elif bendList == [0,1,0]:
        deconvertedBend = "+y"
    elif bendList == [0,-1,0]:
        deconvertedBend = "-y"
    elif bendList == [1,0,0]:
        deconvertedBend = "+x"
    elif bendList == [-1,0,0]:
        deconvertedBend = "-x"
    return deconvertedBend

LArray = []
bendsArray = []
results = []

L = int(input())
while L != 0:
    LArray.append(L)
    bendsArray.append(input())
    L = int(input())

for LIndex in range(len(LArray)):
    L = LArray[LIndex]
    bends = bendsArray[LIndex]
    bendsList=bends.split(' ')
    previousDirection = [1,0,0]
    currentDirection = [1,0,0]
    counters = [0,0,0]
    auxBend = [0,-0,0]
    modificado = False
    bendDimension = -1
    bendDirection = 0
    for i in range(0, L-1):
        directionChanged=False
        currentBend = convertBend(bendsList[i])
        if bendsList[i]!="No":

            for l in range(len(currentBend)):
                if currentBend[l]!=0:
                    bendDimension=l
                if currentBend[l]==1:
                    bendDirection=1
                elif currentBend[l]==-1:
                    bendDirection=-1
            
            #Check if current direction is a normal vector to movement plane
            auxBend[0]=1
            for n in range(1, len(currentBend)):
                auxBend[n]=currentBend[n]
            k=0
            modificado=False
            while k < len(currentBend):
                if modificado == False:
                    #Check if direction is a tangent vector to movement plane
                    if (abs(currentDirection[k]) == abs(auxBend[k])):
                        if abs(auxBend[k])==1:
                            if counters[bendDimension]%4==0:
                                #Copy currentDirection into previousDirection
                                for n in range(len(previousDirection)):
                                    previousDirection[n]=currentDirection[n]
                                for m in range(len(currentDirection)):
                                    currentDirection[m]=currentBend[m]*bendDirection
                            elif counters[bendDimension]%4==1:
                                for m in range(len(currentDirection)):
                                    currentDirection[m]=previousDirection[m]*-1*bendDirection
                                #Copy currentDirection into previousDirection
                                for n in range(len(previousDirection)):
                                    previousDirection[n]=currentDirection[n]
                            elif counters[bendDimension]%4==2:
                                #Copy currentDirection into previousDirection
                                for n in range(len(previousDirection)):
                                    previousDirection[n]=currentDirection[n]
                                for m in range(len(currentDirection)):
                                    currentDirection[m]=currentBend[m]*-1*bendDirection
                            elif counters[bendDimension]%4==3:
                                for m in range(len(currentDirection)):
                                    currentDirection[m]=previousDirection[m]*bendDirection
                                #Copy currentDirection into previousDirection
                                for n in range(len(previousDirection)):
                                    previousDirection[n]=currentDirection[n]
                            modificado=True
                k=k+1
            #Increment counter
            for j in range(len(counters)):
                counters[j]=counters[j]+currentBend[j]
    results.append(deconvertBend(currentDirection))

for result in results:
    print(result)