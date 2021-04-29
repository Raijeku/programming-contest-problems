string = input()
RFP_num = 1
selected_proposals = []
while string!='0 0':
    string = string.split()
    n = int(string[0])
    p = int(string[1])
    requirements = []
    proposals = []
    prices = []
    compliant = [-1]*p
    partially_compliant = [-1]*p
    for i in range(n):
        requirements.append(input())
    for i in range(p):
        proposals.append(input())
        string = input().split()
        r = int(string[1])
        prices.append(float(string[0]))
        for j in range(r):
            input()
        if r == n:
            compliant[i] = prices[-1]
        else:
            partially_compliant[i] = r/n
    max_compliance = max(partially_compliant)
    if partially_compliant.count(max_compliance)==1:
        selected = partially_compliant.index(max_compliance)
    elif compliant.count(min(compliant))==1:
        selected = compliant.index(min(compliant))
    else:
        selected = 0
    selected_proposals.append(proposals[selected])

    string = input()

for proposal in selected_proposals:
    print('RFP #{0}'.format(RFP_num))
    print(proposal+"\n")
    RFP_num += 1