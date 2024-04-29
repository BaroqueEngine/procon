N, L = map(int, input().split())
X = set(list(map(int, input().split())))
T = list(map(int, input().split()))

dp = [10**18] * (L + 10)
dp[0] = 0

for i in range(L):
    K = T[2] if i + 1 in X else 0
    dp[i + 1] = min(dp[i + 1], dp[i] + T[0] + K)
    K = T[2] if i + 2 in X else 0
    dp[i + 2] = min(dp[i + 2], dp[i] + T[0] + T[1] + K)
    K = T[2] if i + 4 in X else 0
    dp[i + 4] = min(dp[i + 4], dp[i] + T[0] + T[1] * 3 + K)
dp[L] = min(dp[L], dp[L - 1] + (T[0] + T[1]) // 2)
dp[L] = min(dp[L], dp[L - 2] + T[0] // 2 + T[1] + T[1] // 2)
if L >= 3:
    dp[L] = min(dp[L], dp[L - 3] + T[0] // 2 + T[1] * 2 + T[1] // 2)

print(dp[L])
