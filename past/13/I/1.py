import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)

seen = [False] * N
finished = [False] * N


def dfs(cur):
    if seen[cur]:
        if not finished[cur]:
            print("No")
            exit()
        else:
            return
    seen[cur] = True
    for next in G[cur]:
        dfs(next)
    finished[cur] = True


for i in range(N):
    if seen[i]:
        continue
    dfs(i)

print("Yes")
