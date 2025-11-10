N = int(input())
W_MAX = 500 * 500 + 1
dp = [-1] * W_MAX
dp[0] = 0
total_w = 0

for i in range(N):
    W, H, B = map(int, input().split())
    total_w += W
    idp = dp[:]
    for j in range(W_MAX):
        if dp[j] == -1:
            continue
        idp[j + W] = max(idp[j + W], dp[j] + B)
        idp[j] = max(idp[j], dp[j] + H)
    dp = idp[:]

ans = 0
for i in range(W_MAX - 1, -1, -1):
    if dp[i] == -1:
        continue
    if i < total_w - i:
        continue
    ans = max(ans, dp[i])

print(ans)