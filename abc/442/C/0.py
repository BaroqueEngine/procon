N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

def f(x):
    return x * (x - 1) * (x - 2) // 6

ans = []
for i in range(N):
    ans.append(f(N - len(G[i]) - 1))

print(*ans)