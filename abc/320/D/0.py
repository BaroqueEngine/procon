import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, X, Y))
    G[B].append((A, -X, -Y))

pos = [""] * N
pos[0] = (0, 0)

seen = [False] * N


def f(cur, x, y):
    seen[cur] = True
    pos[cur] = (x, y)
    for next, tx, ty in G[cur]:
        if seen[next]:
            continue
        f(next, x + tx, y + ty)


f(0, 0, 0)

for p in pos:
    print("undecidable" if p == "" else "{0} {1}".format(p[0], p[1]))
