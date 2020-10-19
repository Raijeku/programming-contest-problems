import sys
import math

def path_distance_recursive(distances,origin,index,indexes,path_distance,paths):
    print("Position is:",origin,",",index,"with path_distance",path_distance)
    if index not in indexes:
        indexes.append(index)
        if origin not in indexes:
            indexes.append(origin)
        if origin == len(distances)-3:
            path_distance += distances[origin][index]
            paths.append(path_distance)
        else:
            for i in range(origin+2,len(distances)):
                indexes = []
                path_distance_recursive(distances, origin+1, i,indexes, path_distance+distances[origin][index],paths)
    return path_distance

def path_distance_recursive_2(distances,origin,index,indexes,path_distance,paths):
    print("Position is:",origin,",",index,"with path_distance",path_distance)
    if origin < len(distances)-3:
        for i in range(origin+2,len(distances)):
            indexes = []
            path_distance_recursive(distances, origin+1, i,indexes, path_distance+distances[origin][index],paths)
    if index not in indexes and origin not in indexes:
        indexes.append(index)
        indexes.append(origin)
        if origin == len(distances)-3:
            path_distance += distances[origin][index]
            paths.append(path_distance)
            
    return path_distance

students = []
indexes = []
is_n = True
i=0
distance = 0
min_distance = 10000
total_distance = 0
min_i = -1
min_j = -1

for line in sys.stdin:
    if is_n==True:
        n = int(line)
        is_n=False
        if n==0:
            break
    elif i < 2*n:
        new_line = line.split(' ')
        students.append((new_line[0],int(new_line[1]),int(new_line[2].replace('\n',''))))
        i+=1
        if i == 2*n:
            i=0
            is_n=True

print(students)

distances = []

for i in range(len(students)):
    aux = []
    for j in range(i+1):
        aux.append(1000001)
    for j in range(i+1,len(students)):    
        aux.append(((students.copy()[i][1]-students.copy()[j][1])**2 + (students.copy()[i][2]-students.copy()[j][2])**2)**0.5)  
    distances.append(aux)

print(distances)
found = False

'''for i in range(len(students)):
    min_distance = 1000001
    found = False
    for j in range(len(students)):
        if i>j and not i in indexes and not j in indexes:
            distance = distances[i][j]
            if distance < min_distance and distance != 0:
                min_distance=distance
                min_i=i
                min_j=j
                found = True'''

paths = []
for i in range(1,len(students)):
    indexes = []
    path_distance_recursive_2(distances,0,i,indexes,0,paths)
print(paths)
print(len(paths))


for i in range(len(paths)):
    if paths[i] < min_distance:
        min_distance = paths[i]
print(min_distance)

'''min_distance = 1000001
    found = False
    for j in range(len(students)):
        if i>j and not i in indexes and not j in indexes:
            distance = distances[i][j]
            if distance < min_distance and distance != 0:
                min_distance=distance
                min_i=i
                min_j=j
                found = True'''



'''if found:            
        indexes.append(min_i)
        indexes.append(min_j)
        total_distance += min_distance'''
    #print(total_distance)

    
#print(total_distance)