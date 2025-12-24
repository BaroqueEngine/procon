N, M = map(int, input().split())

visited = set([])
for _ in range(M):
    Y, X = map(int, input().split())
    X -= 1
    Y -= 1
    if X >= N - 1 or Y >= N - 1:
        continue
    ok = True
    for ty in range(Y, Y + 2):
        for tx in range(X, X + 2):
            if (tx, ty) in visited:
                ok = False
    if ok:
        for ty in range(Y, Y + 2):
            for tx in range(X, X + 2):
                visited.add((tx, ty))

print(len(visited) // 4)