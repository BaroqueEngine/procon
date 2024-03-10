import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())
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
    if x == y:
        return

    par[x] += par[y]
    par[y] = x


for _ in range(Q):
    type, u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    if type == 1:
        unite(u, v)
    else:
        print("Yes" if same(u, v) else "No")
