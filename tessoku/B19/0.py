N, MAX_W = map(int, input().split())
A = []
for _ in range(N):
    W, V = map(int, input().split())
    A.append((W, V))

INF = 100000000000000000
dp = [INF] * 100001
dp[0] = 0

for w, v in A:
    idp = dp[:]
    for j in range(100000, -1, -1):
        if j - v >= 0 and idp[j - v] != INF:
            idp[j] = min(idp[j], idp[j - v] + w)
    dp = idp[:]

ans = 0
for i in range(len(dp)):
    if dp[i] <= MAX_W:
        ans = i
print(ans)
