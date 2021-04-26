n = int(input())
for i in range(n):
    string = input().split()
    if int(string[0]) < int(string[1]):
        print('<')
    elif int(string[0]) > int(string[1]):
        print('>')
    else:
        print('=')