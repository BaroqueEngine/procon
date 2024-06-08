N, M = map(int, input().split())
INF = 10**18
G = [[INF] * N for _ in range(N)]
for i in range(N):
    G[i][i] = 0

ans = []
for _ in range(M):
    Q = list(map(int, input().split()))
    if Q[0] == 0:
        u, v = Q[1:]
        u -= 1
        v -= 1
        ans.append(G[u][v])
    else:
        u, v, cost = Q[1:]
        u -= 1
        v -= 1
        G[u][v] = G[v][u] = min(G[u][v], cost)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for x in ans:
    if x == INF:
        x = -1
    print(x)
