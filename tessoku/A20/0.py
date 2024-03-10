S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for y in range(1, len(S) + 1):
    for x in range(1, len(T) + 1):
        dp[y][x] = max(dp[y][x], dp[y][x - 1])
        dp[y][x] = max(dp[y][x], dp[y - 1][x])
        if S[y - 1] == T[x - 1]:
            dp[y][x] = max(dp[y][x], dp[y - 1][x - 1] + 1)

print(max(dp[-1]))
