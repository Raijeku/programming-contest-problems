T = int(input())
for i in range(T):
    numbers = input().split()
    speed = 0
    for j in range(len(numbers)-1):
        if int(numbers[j+1])>speed:
            speed = int(numbers[j+1])
    print('Case {0}: {1}'.format(i+1, speed))