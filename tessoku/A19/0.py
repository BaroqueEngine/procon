N, MAX_W = map(int, input().split())
A = []
for _ in range(N):
    W, V = map(int, input().split())
    A.append((W, V))

dp = [-1] * (MAX_W + 1)
dp[0] = 0

for i in range(N):
    w, v = A[i]
    idp = dp[:]
    for j in range(MAX_W, -1, -1):
        if j - w >= 0 and idp[j - w] != -1:
            idp[j] = max(idp[j], idp[j - w] + v)
    dp = idp[:]

print(max(dp))
