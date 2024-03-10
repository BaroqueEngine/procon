import sys
N = int(input())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append(V)
    G[V].append(U)

sys.setrecursionlimit(10**7)


def f(cur, prev):
    ret = 0
    for next in G[cur]:
        if next == prev:
            continue
        ret += f(next, cur)
    return ret + 1


ans = 0
max_child = 0
for start in G[0]:
    n = f(start, 0)
    ans += n
    max_child = max(max_child, n)
print(ans - max_child + 1)
