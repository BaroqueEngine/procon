N = int(input())
A = list(map(int, input().split()))
ans = 0

dp = {}
for x in A:
    dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)
    ans = max(ans, dp[x])

print(ans)