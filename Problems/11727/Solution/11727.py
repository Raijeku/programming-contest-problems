n = int(input())
for i in range(n):
    string = input().split()
    numbers = [int(string_number) for string_number in string]
    numbers.sort()
    print('Case {0}: {1}'.format(i+1, str(numbers[1])))
    #for i in range(string):
    #    string[i] = int(string[i])
    
    '''least_count = 0
    least = 10001
    for j in range(3):
        if int(string[j]) < least:
            least = int(string[j])
            least_count += 1
        if least_count == 2:
            print('Case {0}: {1}'.format(i, least))
            break'''
