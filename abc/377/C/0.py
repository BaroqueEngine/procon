N, M = map(int, input().split())

seen = set()
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(M):
    x, y = map(int, input().split())
    seen.add((x, y))

    for i in range(len(dx)):
        tx = x + dx[i]
        ty = y + dy[i]

        if 1 <= tx <= N and 1 <= ty <= N:
            seen.add((tx, ty))

print(N * N - len(seen))
