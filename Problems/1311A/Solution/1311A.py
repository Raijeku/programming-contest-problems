cases = int(input())
lines = []
for i in range(cases):
    line = input()
    line_vector = line.split(' ')
    a = int(line_vector[0])
    b = int(line_vector[1])
    lines.append([a,b])
for i in range(cases):
    a = lines[i][0]
    b = lines[i][1]
    counter = 0
    while a != b:
        if a<b:
            x = b-a
            if x % 2 == 0:
                x -= 1
            a += x
        else:
            y = a-b
            if y % 2 != 0:
                y += 1
            a -= y
        counter += 1
    print(counter)
    