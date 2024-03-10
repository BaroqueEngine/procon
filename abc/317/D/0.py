N = int(input())
A = []
MAX_Z = 0
tak = 0
aoki = 0
for _ in range(N):
    X, Y, Z = map(int, input().split())
    W = max(0, (Y - X + 1) // 2)
    A.append((X, Y, Z, W))
    MAX_Z += Z

    if X > Y:
        tak += Z
    else:
        aoki += Z

t = max(0, (aoki - tak + 1) // 2)

INF = 10**15
dp = [INF] * (MAX_Z + 1)
dp[0] = 0

for x, y, z, w in A:
    idp = dp[:]
    for i in range(MAX_Z + 1):
        if dp[i] == INF:
            continue
        if i + z <= MAX_Z:
            idp[i + z] = min(idp[i + z], dp[i] + w)
    dp = idp[:]

ans = INF
for i in range(tak + t, MAX_Z + 1):
    ans = min(ans, dp[i])
print(ans)
