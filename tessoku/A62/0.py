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
sys.setrecursionlimit(10**9)
def search(cur):
    for next in G[cur]:
        if seen[next]:
            continue
        seen[next] = True
        search(next)


seen[0] = True
search(0)

print("The graph is connected." if sum(seen) == N else "The graph is not connected.")
