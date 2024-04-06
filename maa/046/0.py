import queue
H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1
M = [input() for _ in range(H)]

dist = [[-1] * W for _ in range(H)]

q = queue.Queue()
q.put((sx, sy, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while not q.empty():
    x, y, step = q.get()

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if M[ty][tx] == "#":
            continue
        if dist[ty][tx] != -1:
            continue
        dist[ty][tx] = step + 1
        q.put((tx, ty, step + 1))

print(dist[gy][gx])
