# 貰うDP

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dp = [[[-1] * (H + W) for __ in range(W)] for _ in range(H)]

for y in range(H):
    for x in range(W):
        dp[y][x][0] = 0
dp[0][0][1] = A[0][0]

for y in range(H):
    for x in range(W):
        if x - 1 >= 0:
            for i in range(H + W - 1, 0, -1):
                dp[y][x][i] = max(dp[y][x][i], dp[y][x - 1][i])
                dp[y][x][i] = max(dp[y][x][i], dp[y][x - 1][i - 1] + A[y][x])
        if y - 1 >= 0:
            for i in range(H + W - 1, 0, -1):
                dp[y][x][i] = max(dp[y][x][i], dp[y - 1][x][i])
                dp[y][x][i] = max(dp[y][x][i], dp[y - 1][x][i - 1] + A[y][x])

for i in range(1, H + W):
    print(dp[-1][-1][i])