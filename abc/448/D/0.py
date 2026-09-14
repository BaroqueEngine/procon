import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append(V)
    G[V].append(U)

results = [False] * N

def f(cur, prev, hist):
    if prev != -1 and results[prev]:
        results[cur] = True
    else:
        results[cur] = hist[A[cur]] >= 1

    for next in G[cur]:
        if next == prev:
            continue
        hist[A[cur]] += 1
        f(next, cur, hist)
        hist[A[cur]] -= 1

f(0, -1, defaultdict(int))

for x in results:
    print("Yes" if x else "No")