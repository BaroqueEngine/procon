N, A, B = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

INF = 10**18
dp = [[-INF] * (B + 1) for _ in range(A + 1)]
dp[0][0] = 0


for w, v in items:
    idp = []
    for line in dp:
        idp.append(line[:])

    for i in range(A + 1):
        for j in range(B + 1):
            x = dp[i - w][j] + v if i - w >= 0 and dp[i - w][j] != -INF else -INF
            y = dp[i][j - w] + v if j - w >= 0 and dp[i][j - w] != -INF else -INF
            z = dp[i][j]
            idp[i][j] = max(idp[i][j], x, y, z)

    dp = []
    for line in idp:
        dp.append(line[:])

ans = -INF
for line in dp:
    ans = max(ans, max(line))
print(ans)