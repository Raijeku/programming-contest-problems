while True:
    try:
        string_vec = input().split()
        N = int(string_vec[0])
        B = int(string_vec[1])
        H = int(string_vec[2])
        W = int(string_vec[3])
        total_cost = 0
        occupation = [-1]*W
        ps = []
        #hotel_info = []
        for i in range(H):
            p = int(input())
            ps.append(p)
            weeks = input().split()
            for j in range(W):
                if int(weeks[j]) >= N and occupation[j]==-1:
                    occupation[j] = i
        for i in range(W):
            total_cost += ps[occupation[i]]
        if total_cost<=B and -1 not in occupation: print(total_cost)
        else: print('stay home')
    except EOFError:
        break