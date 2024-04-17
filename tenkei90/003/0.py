N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

def f(start):
    stack = [(start, -1, 0)]
    best_index = None
    best_dist = 0
    while len(stack) > 0:
        cur, prev, dist = stack.pop()
        if dist > best_dist:
            best_dist = dist
            best_index = cur
        for next in G[cur]:
            if next == prev:
                continue
            stack.append((next, cur, dist + 1))
    return (best_index, best_dist)

print(f(f(1)[0])[1] + 1)