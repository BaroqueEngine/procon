N = int(input())
A = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]
dp[1][0] = A[0]
for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
    dp[1][i] = dp[0][i - 1] + A[i]

print(max(dp[0][-1], dp[1][-1]))
