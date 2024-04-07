N = int(input())
H = list(map(int, input().split()))

INF = 10**18
dp = [INF] * N
dp[0] = 0

for i in range(N):
    for j in range(1, 3):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + abs(H[i] - H[i + j]))

print(dp[-1])
