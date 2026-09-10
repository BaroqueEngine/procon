N, M = map(int, input().split())

par = [-1] * N
size = [1] * N

def root(x):
    if par[x] == -1:
        return x
    par[x] = root(par[x])
    return par[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)

    if same(x, y):
        return

    if size[y] > size[x]:
        x, y = y, x

    par[y] = x
    size[x] += size[y]

G = []
for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    G.append((U, V))

MOD = 998244353
ans = 0
cnt = N

for i in range(M - 1, -1, -1):
    u, v = G[i]
    if same(u, v):
        continue
    if cnt <= 2:
        ans = (ans + pow(2, i + 1, MOD)) % MOD
    else:
        unite(u, v)
        cnt -= 1

print(ans)
