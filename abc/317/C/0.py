N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))

import sys

sys.setrecursionlimit(10**7)

seen = [False] * True
seen[0] = True
start = 0


def f(cur, dist, seen):
    ret = dist
    for next, next_dist in G[cur]:
        if seen[next]:
            continue
        new_seen = seen[:]
        new_seen[next] = True
        ret = max(ret, f(next, dist + next_dist, new_seen))
    return ret


ans = []
for i in range(N):
    seen = [False] * N
    seen[i] = True
    ans.append(f(i, 0, seen))
print(max(ans))
