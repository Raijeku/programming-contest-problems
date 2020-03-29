n, d = input().split(" ")
n = int(n)
d = int(d)
r = list()
while n!=0 or d!=0:
    r.append(pow(n,d))
    n, d = input().split(" ")
    n = int(n)
    d = int(d)
for elem in r:
    print(elem)