N, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
SIZE = N * 1000 + 1
INF = 10**18
dp = [INF] * SIZE
dp[0] = 0

for w, v in A:
    idp = dp[:]
    for i in range(SIZE):
        if dp[i] != INF:
            idp[i + v] = min(idp[i + v], dp[i] + w)
    dp = idp[:]

for i in range(SIZE - 1, -1, -1):
    if dp[i] <= W:
        print(i)
        exit()
