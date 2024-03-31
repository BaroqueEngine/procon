N = int(input())
H = list(map(int, input().split()))
INF = 10**18
dp = [INF] * N
dp[0] = 0
prev = [-1] * N

for i in range(N):
    if i + 1 < N:
        temp = dp[i + 1]
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i] - H[i + 1]))
        if temp != dp[i + 1]:
            prev[i + 1] = i
    if i + 2 < N:
        temp = dp[i + 2]
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i] - H[i + 2]))
        if temp != dp[i + 2]:
            prev[i + 2] = i

route = [N - 1]
while route[-1] != 0:
    route.append(prev[route[-1]])

print(len(route))
print(*[x + 1 for x in route[::-1]])
