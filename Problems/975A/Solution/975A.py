length = int(input())
strings = input()
words = strings.split(' ')
counters = []
root_indexes = []
for word in words:
    dictionary = {}
    for letter in word:
        if letter in dictionary.keys():
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    counters.append(dictionary)

for i, counter in enumerate(counters):
    is_in = False
    for index in root_indexes:
        if counter == counters[index]:
            is_in = True
    if not is_in:
        root = True
        for key in counter:
            if counter[key]!=1:
                root = False
        if root == True:
            root_indexes.append(i)
for i in range(len(words)):
    if i not in root_indexes:
        contained = []
        for index in root_indexes:
            actual_contained = True
            for j in range(len(words[i])):
                if words[i][j] not in words[index]:
                    actual_contained = False
            contained.append(actual_contained)
        if True not in contained:
            root_indexes.append(index)

print(len(root_indexes))
    