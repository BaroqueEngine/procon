import sys
sys.setrecursionlimit(10**7)

N, X = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))

def dfs(cur, prev, dist):
    if dist == X:
        print("Yes")
        exit()
    for next, cost in G[cur]:
        if next == prev:
            continue
        dfs(next, cur, dist + cost)

for i in range(N):
    dfs(i, -1, 0)

print("No")