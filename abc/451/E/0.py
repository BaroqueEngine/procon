import sys
sys.setrecursionlimit(10**6)

N = int(input())
T = [[0] * N for _ in range(N)]
stack = []

for i in range(N - 1):
    A = list(reversed(list(map(int, input().split()))))
    for j in range(i + 1, N):
        cost = A.pop()
        stack.append((cost, i, j))
        T[i][j] = cost
        T[j][i] = cost

stack.sort(reverse=True)
par = [-1] * N

def root(x):
    if par[x] < 0:
        return x
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

G = [[] for _ in range(N)]

while len(stack) > 0:
    cost, u, v = stack.pop()
    if same(u, v):
        continue
    unite(u, v)
    G[u].append((v, cost))
    G[v].append((u, cost))

def dfs(cur, prev, dist, base):
    T[base][cur] -= dist

    for next, cost in G[cur]:
        if next == prev:
            continue
        dfs(next, cur, dist + cost, base)

for i in range(N):
    dfs(i, -1, 0, i)

ok = True
for y in range(N):
    for x in range(N):
        if T[y][x] != 0:
            ok = False

print("Yes" if ok else "No")