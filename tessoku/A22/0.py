N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

INF = 10**10
dp = [-INF] * (N + 1)
dp[1] = 0

for i in range(1, N):
    if dp[i] == -INF:
        continue
    dp[A[i]] = max(dp[A[i]], dp[i] + 100)
    dp[B[i]] = max(dp[B[i]], dp[i] + 150)

print(dp[N])
