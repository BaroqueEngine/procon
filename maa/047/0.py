import sys
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

color = [-1] * N

sys.setrecursionlimit(10**7)


def f(cur, v):
    color[cur] = v
    for next in G[cur]:
        if color[next] == v:
            print("No")
            exit()
        if color[next] == -1:
            f(next, 1 - v)


for i in range(N):
    if color[i] == -1:
        f(i, 0)
print("Yes")
