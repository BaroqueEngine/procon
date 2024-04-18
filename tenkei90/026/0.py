import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

start = None
for i in range(1, N + 1):
    if len(G[i]) == 1:
        start = i
        break

ans = []


def f(cur, prev=-1, pick=True):
    if pick and len(ans) < N // 2:
        ans.append(cur)
    for next in G[cur]:
        if next == prev:
            continue
        f(next, cur, not pick)


f(start)
if len(ans) == N // 2:
    print(*sorted(ans))
else:
    ans = []
    f(start, -1, False)
    print(*sorted(ans))
