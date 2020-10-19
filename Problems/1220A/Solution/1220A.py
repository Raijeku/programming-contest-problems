length = int(input())
string = input()
contador_0 = 0
contador_1 = 0
for letter in string:
    if letter == 'z':
        contador_0 += 1
    elif letter == 'n':
        contador_1 += 1
string = ''
for contador in range(contador_1):
    string += '1 '
for contador in range(contador_0):
    string += '0 '
string=''.join(list(string)[:-1])
print(string)