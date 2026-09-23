import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)

seen = [False] * N
seen[0] = True

def f(cur):
    for next in G[cur]:
        if seen[next]:
            continue
        seen[next] = True
        f(next)
f(0)

print(sum(seen))