import sys
sys.setrecursionlimit(10**7)

start = None
N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    P = int(input())
    if P == -1:
        start = i
        continue
    G[P - 1].append(i)

order = []
pos = [None] * N
size = [None] * N


def dfs(cur):
    pos[cur] = len(order)
    order.append(cur)
    for next in G[cur]:
        dfs(next)
    size[cur] = len(order) - pos[cur] - 1


dfs(start)

ans = []
Q = int(input())
for i in range(Q):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    ans.append("Yes" if pos[B] < pos[A] <= pos[B] + size[B] else "No")

for x in ans:
    print(x)
