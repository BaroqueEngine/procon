N = int(input())
A = list(map(int, input().split()))
INF = 10**18
dp = [[[INF] * (sum(A) + 1) for _ in range(sum(A) + 1)] for __ in range(N)]
dp[0][sum(A)][0] = 0
for i in range(1, N - 1):
    for f in range(sum(A) + 1):
        for t in range(sum(A) + 1):
            if dp[i - 1][f][t] != INF:
                for k in range(f + 1):
                    dx = 1
                    dy = t - k
                    dist = (dx * dx + dy * dy) ** 0.5
                    dp[i][f - k][k] = min(dp[i][f - k][k],
                                          dp[i - 1][f][t] + dist)

for i in range(sum(A) + 1):
    if dp[-2][0][i] != INF:
        dx = 1
        dy = i
        dist = (dx * dx + dy * dy) ** 0.5
        dp[-1][0][0] = min(dp[-1][0][0], dp[-2][0][i] + dist)
print(dp[-1][0][0])
