import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G[X].append(Y)
    RG[Y].append(X)

reachable = [False] * N

def fill(cur):
    reachable[cur] = True
    for next in RG[cur]:
        if reachable[next]:
            continue
        fill(next)

ans = []
Q = int(input())
for _ in range(Q):
    T, V = map(int, input().split())
    V -= 1
    if T == 1:
        if reachable[V]:
            continue
        fill(V)
    else:
        ans.append("Yes" if reachable[V] else "No")

for x in ans:
    print(x)