N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
time = set()
for _, b, _ in A:
    time.add(b)
time = sorted(list(time))
time_order = {}
for i in range(len(time)):
    time_order[time[i]] = i + 1

for i in range(N):
    A[i][1] = time_order[A[i][1]]
A.sort(key=lambda arr: arr[1])

INF = 10**18
dp = [[INF] * (M + 1) for _ in range(A[-1][1] + 1)]
dp[0][0] = 0

for a, b, c in A:
    for i in range(M + 1):
        dp[b][i] = min(dp[b][i], dp[b - 1][i])
        if dp[b - 1][i] != INF:
            dp[b][min(i + c, M)] = min(dp[b][min(i + c, M)], dp[b - 1][i] + a)

if dp[-1][M] == INF:
    dp[-1][M] = -1
print(dp[-1][M])
