import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())
par = [-1] * N
rank = [1] * N


def root(x):
    if par[x] == -1:
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

    if rank[x] > rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[y] += 1

    par[x] = y


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        unite(query[1] - 1, query[2] - 1)
    else:
        print("Yes" if same(query[1] - 1, query[2] - 1) else "No")
