N = int(input())
A = list(map(int, input().split()))

INF = 10**18
dp = [[INF] * N for _ in range(2)]

# dp[0] = 休み
# dp[1] = 勉強
dp[0][0] = 0
dp[1][0] = A[0]

for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
    dp[1][i] = max(dp[0][i - 1] + A[i], dp[1][i - 1])

print(max(dp[0][-1], dp[1][-1]))
