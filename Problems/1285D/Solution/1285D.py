def max(array):
    max_value = -1
    for value in array:
        if value > max_value:
            max_value = value
    return max_value


length = int(input())
line = input()
line_array = line.split(' ')
integers = [int(line_array[i]) for i in range(length)]
max_int = max(integers)
base = 0
print("here1")
while (max_int!=0):
    base += 1
    max_int //= 2
largest = (2**base)
#largest = max_int
print("here2")

operated_integers = []
for X in range(largest):
    operated_integers.append([integer ^ X for integer in integers])
    print("here 2.5")
print("here3")
mins = [max(operated_integers[i]) for i in range(len(operated_integers))]
print("here4")
min_value = 2**30
for value in mins:
    if value < min_value:
        min_value = value
    print("each here")
print(min_value)