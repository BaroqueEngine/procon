from itertools import permutations

N, S, T = map(int, input().split())
G = []
for i in range(N):
    A, B, C, D = map(int, input().split())
    G.append(((A, B), (C, D)))

ans = 10**18
for p in permutations(G):
    for bit in range(2**N):
        order = []
        for i in range(N):
            order.append((bit >> i) & 1)
        route = []
        total = 0
        x, y = 0, 0
        for u, v in p:
            if order.pop():
                u, v = v, u
            route.append((u, v))
            dx = u[0] - x
            dy = u[1] - y
            dist = (dx * dx + dy * dy) ** 0.5
            total += dist / S

            dx = u[0] - v[0]
            dy = u[1] - v[1]
            dist = (dx * dx + dy * dy) ** 0.5
            total += dist / T

            x, y = v[0], v[1]
        ans = min(ans, total)

print(ans)
