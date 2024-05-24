import queue

H, W = map(int, input().split())
S = [input() for _ in range(H)]

sx, sy, gx, gy, ax, ay = None, None, None, None, None, None
for y in range(H):
    for x in range(W):
        if S[y][x] == "s":
            sx, sy = x, y
            S[y][x] == "."
        if S[y][x] == "g":
            gx, gy = x, y
            S[y][x] == "."
        if S[y][x] == "a":
            ax, ay = x, y
            S[y][x] == "."

dist = [[[[-1] * W for _ in range(H)] for __ in range(W)] for ___ in range(H)]
dist[sy][sx][ay][ax] = 0

q = queue.Queue()
q.put((sx, sy, ax, ay))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while not q.empty():
    x, y, box_x, box_y = q.get()

    if box_x == gx and box_y == gy:
        print(dist[y][x][box_y][box_x])
        exit()

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if S[ty][tx] == "#":
            continue
        if tx == box_x and ty == box_y:
            box_tx = box_x + dx[i]
            box_ty = box_y + dy[i]
            if box_tx < 0 or box_tx >= W or box_ty < 0 or box_ty >= H:
                continue
        else:
            box_tx = box_x
            box_ty = box_y
        if S[box_ty][box_tx] == "#":
            continue
        if dist[ty][tx][box_ty][box_tx] != -1:
            continue
        dist[ty][tx][box_ty][box_tx] = dist[y][x][box_y][box_x] + 1
        q.put((tx, ty, box_tx, box_ty))
print(-1)