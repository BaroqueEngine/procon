import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

seen = [False] * N
num = 0
edge = 0


def f(cur):
    global num, edge
    seen[cur] = True
    num += 1
    for next in G[cur]:
        if cur < next:
            edge += 1
        if seen[next]:
            continue
        f(next)


def nC2(x):
    return x * (x - 1) // 2


ans = -M
for i in range(N):
    if not seen[i]:
        num = 0
        edge = 0
        f(i)
        ans += nC2(num)

print(ans)
