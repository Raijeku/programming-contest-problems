n = int(input())
for i in range(n):
    string = input().split()
    numbers = [int(string_number) for string_number in string]
    numbers.sort()
    print('Case {0}: {1}'.format(i+1, str(numbers[1])))