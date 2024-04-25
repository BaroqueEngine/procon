N, M = map(int, input().split())

par = []


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


L = []
S = []

for _ in range(N):
    X, Y, C = map(int, input().split())
    L.append((X, Y, C))

for _ in range(M):
    X, Y, C = map(int, input().split())
    S.append((X, Y, C))


def f(A):
    edges = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            x1, y1, c1 = A[i]
            x2, y2, c2 = A[j]
            k = 1 if c1 == c2 else 10
            dx = x1 - x2
            dy = y1 - y2
            cost = (dx * dx + dy * dy) ** 0.5
            cost *= k
            edges.append((cost, i, j))
    edges.sort()

    global par
    par = [-1] * len(A)
    ret = 0
    for cost, i, j in edges:
        if not same(i, j):
            unite(i, j)
            ret += cost
    return ret


ans = 10**18
for bit in range(2 ** M):
    use = []
    for i in range(M):
        if bit >> i & 1 == 1:
            use.append(i)
    A = L[::]
    for i in use:
        A.append(S[i])
    ans = min(ans, f(A))
print(ans)
