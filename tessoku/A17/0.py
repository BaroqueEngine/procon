N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [10**9] * N
dp[0] = 0

for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + A[i])
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + B[i])

routes = [N - 1]
cur = N - 1

while cur > 0:
    if dp[cur] - A[cur - 1] == dp[cur - 1]:
        routes.append(cur - 1)
        cur -= 1
    else:
        routes.append(cur - 2)
        cur -= 2

routes = routes[::-1]
print(len(routes))
print(*[x + 1 for x in routes])