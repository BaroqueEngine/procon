N, M, Q = map(int, input().split())
all = [False] * (N + 1)
kengen = [set([]) for _ in range(N + 1)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        kengen[query[1]].add(query[2])
    elif query[0] == 2:
        all[query[1]] = True
    else:
        if all[query[1]] or query[2] in kengen[query[1]]:
            print("Yes")
        else:
            print("No")