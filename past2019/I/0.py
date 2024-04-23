N, M = map(int, input().split())


def convert(s):
    ret = 0
    k = 1
    for c in s:
        if c == "Y":
            ret += k
        k *= 2
    return ret


INF = 10**18
dp = [INF] * (2 ** N)
dp[0] = 0

for _ in range(M):
    S, C = input().split()
    S = convert(S)
    C = int(C)
    idp = dp[:]
    for j in range(2 ** N):
        if dp[j] == INF:
            continue
        idp[j | S] = min(idp[j | S], idp[j] + C)
    dp = idp[:]

if dp[-1] == INF:
    dp[-1] = -1
print(dp[-1])
