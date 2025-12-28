N = int(input())
A = [list(map(int, input().split())) for _ in range(3)]

dp = [[-1] * N for _ in range(3)]
dp[0][0] = 0

for y in range(3):
    for x in range(N):
        if dp[y][x] == -1:
            continue
        if x + 1 < N:
            dp[y][x + 1] = max(dp[y][x + 1], dp[y][x] + A[y][x])
        if y + 1 < 3 and x + 1 < N:
            dp[y + 1][x + 1] = max(dp[y + 1][x + 1], dp[y][x] + A[y][x])

print(dp[-1][-1] + A[-1][-1])