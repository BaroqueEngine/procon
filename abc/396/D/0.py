import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    U, V, W = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append((V, W))
    G[V].append((U, W))

def f(cur, hist, v):
    if cur == N - 1:
        return v
    
    ret = 10**20
    for next, w in G[cur]:
        if next in hist:
            continue
        ret = min(ret, f(next, hist + [next], v ^ w))
    return ret

print(f(0, [0], 0))
