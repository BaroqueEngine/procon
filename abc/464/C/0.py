N, M = map(int, input().split())
imos = [[] for _ in range(M)]

for _ in range(N):
    A, D, B = map(int, input().split())
    A -= 1
    D -= 1
    B -= 1
    
    if D == 0 or A == B:
        imos[0].append((1, B))
    else:
        imos[0].append((1, A))
        imos[D].append((-1, A))
        imos[D].append((1, B))

colors = [0] * N
kind = 0

for i in range(M):
    imos[i].sort()
    for sign, color in imos[i]:
        colors[color] += sign
        if colors[color] == 1 and sign == 1:
            kind += 1
        elif colors[color] == 0 and sign == -1:
            kind -= 1
    print(kind)