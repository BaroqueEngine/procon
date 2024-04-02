N, T = map(int, input().split())
T -= 1
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

import sys
sys.setrecursionlimit(10**7)

grade = [0] * N

def f(cur, prev = -1):
    ret = 0
    has_child = False
    for next in G[cur]:
        if next == prev:
            continue
        ret = max(ret, f(next, cur))
        has_child = True
    if has_child:
        ret += 1
    grade[cur] = ret
    return ret

f(T)
print(*grade)