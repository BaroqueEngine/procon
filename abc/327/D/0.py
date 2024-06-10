import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
    A[i] -= 1
    B[i] -= 1
    if A[i] == B[i]:
        print("No")
        exit()
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

hist = [-1] * N


def dfs(cur, color):
    hist[cur] = color
    for next in G[cur]:
        if hist[next] == color:
            print("No")
            exit()
        if hist[next] == -1:
            dfs(next, 1 - color)


for i in range(N):
    if hist[i] == -1:
        dfs(i, 0)
print("Yes")
