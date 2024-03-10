N, M = map(int, input().split())

par = [-1] * N


def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


def same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)

    if same(x, y):
        return

    par[x] += par[y]
    par[y] = x


V = []
for _ in range(M):
    A, B, C = map(int, input().split())
    V.append((C, A - 1, B - 1))
V.sort()

ans = 0
for c, a, b in V:
    if same(a, b):
        continue
    unite(a, b)
    ans += c
print(ans)
