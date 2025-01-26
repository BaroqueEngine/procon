N, X = map(int, input().split())
# dp[3][N][X]
dp = [[[-1] * (X + 1) for _ in range(N + 1)] for _ in range(3)]
for v in range(3):
    dp[v][0][0] = 0

IND = [0, 0, 0]

for _ in range(N):
    v, A, C = map(int, input().split())
    v -= 1
    i = IND[v]
    for j in range(X + 1):
        if dp[v][i][j] == -1:
            continue
        dp[v][i + 1][j] = max(dp[v][i + 1][j], dp[v][i][j])
        if j + C <= X:
            dp[v][i + 1][j + C] = max(dp[v][i + 1][j + C], dp[v][i][j] + A)
    IND[v] += 1

def f(x):
    ret = 0
    for v in range(3):
        cur = 10**18
        for c in range(X + 1):
            if dp[v][IND[v]][c] >= x:
                cur = min(cur, c)
        ret += cur
    return ret

ok = 0
ng = 10**10
while ng - ok > 1:
    mid = (ng + ok) // 2
    if f(mid) <= X:
        ok = mid
    else:
        ng = mid
print(ok)
