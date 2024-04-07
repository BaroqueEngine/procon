N, MAX_W = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[-1] * (MAX_W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(MAX_W + 1):
        if dp[i][j] == -1:
            continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j + W[i] <= MAX_W:
            dp[i + 1][j + W[i]] = max(dp[i + 1][j + W[i]], dp[i][j] + V[i])

print(max(dp[-1]))
