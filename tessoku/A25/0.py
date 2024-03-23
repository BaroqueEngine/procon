H, W = map(int, input().split())
M = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            continue
        if x + 1 < W:
            dp[y][x + 1] += dp[y][x]
        if y + 1 < H:
            dp[y + 1][x] += dp[y][x]

print(dp[-1][-1])