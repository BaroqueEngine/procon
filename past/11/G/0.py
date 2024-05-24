import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

seen = [False] * N
def dfs(cur):
    seen[cur] = True
    for next in G[cur]:
        if seen[next]:
            continue
        dfs(next)
dfs(0)

print("Yes" if sum(seen) == N else "No")