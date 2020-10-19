name = input()
length = int(input())
lines = []
people = {}
for i in range(length):
    lines.append(input())
for i in range(length):
    line_vector = lines[i].split(' ')
    name_1 = line_vector[0]
    name_2 = line_vector[-2].split("'")[0]
    if line_vector[1] == 'posted':
        factor = 15
    elif line_vector[1] == 'commented':
        factor = 10
    elif line_vector[1] == 'likes':
        factor = 5
    if name_1 not in people.keys():
        people[name_1] = factor
    else:
        people[name_1] += factor
    if name_2 not in people.keys():
        people[name_2] = factor
    else:
        people[name_2] += factor
if name in people.keys():
    people.pop(name)

#print(people)

items = list(people.items())
length = len(items)

counter = 0
while counter < length:
    i = 0
    length_1 = len(people.items())
    higher_person = -1
    higher_name = 'zzzzzzzzzzzzz'
    while i < length_1:
        i_name = items[i][0]
        factor = items[i][1]
        
        if factor > higher_person:
            higher_person = factor
            higher_name = i_name
        elif factor == higher_person:
            if i_name < higher_name:
                higher_name = i_name

        i+=1
    counter += 1
    people.pop(higher_name)
    items = list(people.items())
    print(higher_name)

