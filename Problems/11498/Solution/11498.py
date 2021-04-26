n = int(input())
while n!=0:
    divisa = input().split()
    for i in range(n):
        coords = input().split()
        if int(coords[0])>int(divisa[0]) and int(coords[1])>int(divisa[1]):
            print('NE')
        if int(coords[0])<int(divisa[0]) and int(coords[1])>int(divisa[1]):
            print('NO')
        if int(coords[0])>int(divisa[0]) and int(coords[1])<int(divisa[1]):
            print('SE')
        if int(coords[0])<int(divisa[0]) and int(coords[1])<int(divisa[1]):
            print('SO')
        elif int(coords[0])==int(divisa[0]) or int(coords[1])==int(divisa[1]):
            print('divisa')
    n = int(input())