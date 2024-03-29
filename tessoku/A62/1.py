N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

seen = [False] * N

import sys
sys.setrecursionlimit(10**7)
def f(cur):
    seen[cur] = True
    for next in G[cur]:
        if seen[next]:
            continue
        f(next)

f(0)
print("The graph is connected." if all(seen) else "The graph is not connected.")