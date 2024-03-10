N = int(input())
G = [[0] * (N) for _ in range(N)]
for i in range(N - 1):
    A = list(map(int, input().split()))
    for j in range(len(A)):
        G[i][i + 1 + j] = G[i + 1 + j][i] = A[j]

import sys

sys.setrecursionlimit(10**7)

ans = 0


def f(k, seen):
    global ans
    if all(seen):
        total = 0
        for a, b in k:
            total += G[a][b]
        ans = max(ans, total)
        return

    i = seen.index(False)
    seen[i] = True

    for j in range(i + 1, N):
        if not seen[j]:
            k.append((i, j))
            seen[j] = True
            f(k, seen)
            k.pop()
            seen[j] = False

    seen[i] = False


seen = [False] * N
if N % 2 == 0:
    f([], seen)
else:
    for i in range(N):
        seen[i] = True
        f([], seen)
        seen[i] = False

print(ans)
