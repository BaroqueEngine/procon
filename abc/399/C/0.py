import sys
sys.setrecursionlimit(10**7)

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

    if x == y:
        return

    par[x] += par[y]
    par[y] = x


ans = 0

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1

    if same(U, V):
        ans += 1
    else:
        unite(U, V)

print(ans)