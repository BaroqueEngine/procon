import queue

N, gx, gy = map(int, input().split())
D = 205
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x + D, y + D))

sx = D
sy = D
gx += D
gy += D
W = 410
H = 410

M = [["."] * W for _ in range(H)]
M[sy][sx] = "S"
M[gy][gx] = "G"
for x, y in P:
    M[y][x] = "#"

q = queue.Queue()
q.put((sx, sy))
dist = [[-1] * W for _ in range(H)]
dist[sy][sx] = 0
dx = [1, 0, -1, 1, -1, 0]
dy = [1, 1, 1, 0, 0, -1]

while not q.empty():
    x, y = q.get()
    for i in range(len(dx)):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if M[ty][tx] == "#":
            continue
        if dist[ty][tx] != -1:
            continue
        dist[ty][tx] = dist[y][x] + 1
        q.put((tx, ty))
print(dist[gy][gx])
