N, M = map(int, input().split())
G = []
for _ in range(M):
    A, B = map(int, input().split())
    G.append((A, B))
G.sort(key=lambda x: (x[0] - x[1]))

def ceil(a, b):
    return (a + b - 1) // b

ans = 0
for A, B in G:
    if N < A:
        continue
    diff = A - B
    cnt = ceil(max(N - (A - 1), 0), diff)
    ans += cnt
    N -= diff * cnt

print(ans)