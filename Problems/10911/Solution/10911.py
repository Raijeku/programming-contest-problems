import sys
import math

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

for i in range(len(students)):
    for j in range(len(students)):
        if i!=j and not i in indexes and not j in indexes:
            distance = math.sqrt(math.pow(students[i][1]-students[j][1],2)+math.pow(students[i][2]-students[j][2],2))
            if distance < min_distance:
                min_distance=distance
                min_i=i
                min_j=j
                
    indexes.append(min_i)
    indexes.append(min_j)
    total_distance += distance
    
print(total_distance)