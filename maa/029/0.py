N = int(input())
dp = [0] * (N + 1)
dp[0] = 1

for i in range(N + 1):
    for j in range(1, 3):
        if i + j <= N:
            dp[i + j] += dp[i]
print(dp[-1])
