H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1
M = [list(input()) for _ in range(H)]

INF = -1
dist = [[INF] * W for _ in range(H)]
dist[sy][sx] = 0

import queue
q = queue.Queue()
q.put((sx, sy))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while not q.empty():
    x, y = q.get()

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if M[ty][tx] == "#":
            continue
        if dist[ty][tx] != INF:
            continue
        dist[ty][tx] = dist[y][x] + 1
        q.put((tx, ty))

print(dist[gy][gx])