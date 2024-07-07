import sys
sys.setrecursionlimit(10**7)
N = int(input())
G = [[] for _ in range(N)]
ans = 0
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))
    ans += C * 2


def far_point(start):
    best_dist = 0
    best_index = 0

    stack = [(start, -1, 0)]
    while len(stack) > 0:
        cur, prev, dist = stack.pop()
        for next, cost in G[cur]:
            if next == prev:
                continue
            stack.append((next, cur, dist + cost))
        if best_dist < dist:
            best_dist = dist
            best_index = cur

    return (best_dist, best_index)


best_dist, best_index = far_point(0)
best_dist, best_index = far_point(best_index)
print(ans - best_dist)
