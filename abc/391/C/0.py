N, Q = map(int, input().split())
nest = [1] * N
pos = [x for x in range(N)]
cnt = 0
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1] - 1, query[2] - 1
        nest[H] += 1
        nest[pos[P]] -= 1
        if nest[pos[P]] == 1:
            cnt -= 1
        pos[P] = H
        if nest[H] == 2:
            cnt += 1
    else:
        ans.append(cnt)

for x in ans:
    print(x)