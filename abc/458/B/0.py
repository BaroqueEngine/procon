H, W = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = [[0] * W for _ in range(H)]

for y in range(H):
    for x in range(W):
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            cnt[y][x] += 1

for line in cnt:
    print(*line)