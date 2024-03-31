N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dist = [[0] * N for _ in range(N)]
for u in range(N):
    for v in range(N):
        dx = A[u][0] - A[v][0]
        dy = A[u][1] - A[v][1]
        dist[u][v] = (dx * dx + dy * dy) ** 0.5

INF = 10**18
dp = [[INF] * N for _ in range(2**N)]
dp[1][0] = 0

for bit in range(2 ** N):
    for u in range(N):
        for v in range(N):
            if bit >> u & 1 == 1 and bit >> v & 1 == 0:
                new_bit = bit | 1 << v
                dp[new_bit][v] = min(dp[new_bit][v], dp[bit][u] + dist[u][v])

print(min([dp[-1][v] + dist[v][0] for v in range(N)]))
