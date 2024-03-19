N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [10**9] * N
dp[0] = 0

for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + A[i])
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + B[i])

print(dp[-1])