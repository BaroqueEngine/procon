N, Q = map(int, input().split())
G = [[False] * N for _ in range(N)]

def search(u, v):
    seen = [False] * N
    seen[u] = True
    stack = [u]
    while len(stack):
        cur = stack.pop()
        if cur == v:
            return True
        for next in range(N):
            if cur == next:
                continue
            if not G[cur][next]:
                continue
            if seen[next]:
                continue
            seen[next] = True
            stack.append(next)
    return False

for _ in range(Q):
    t, u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    if t == 1:
        G[u][v] = not G[u][v]
        G[v][u] = not G[v][u]
    else:
        print("Yes" if search(u, v) else "No")