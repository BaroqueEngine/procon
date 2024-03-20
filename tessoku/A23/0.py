N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

INF = 10**18
dp = [INF] * (2 ** N)
dp[0] = 0

for a in A:
    a = "".join(map(str, a))
    v = int(a, 2)
    idp = dp[:]
    for i in range(2 ** N):
        if dp[i] == INF:
            continue
        idp[i | v] = min(idp[i | v], dp[i] + 1)
    dp = idp[:]

if dp[-1] == INF:
    dp[-1] = -1
print(dp[-1])
