H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dirs = "<>^v"

for y in range(H):
    for x in range(W):
        if S[y][x] in dirs:
            i = dirs.find(S[y][x])
            tx = x + dx[i]
            ty = y + dy[i]
            while 0 <= tx < W and 0 <= ty < H and S[ty][tx] in ".!":
                S[ty][tx] = "!"
                tx += dx[i]
                ty += dy[i]
        elif S[y][x] == "S":
            sx, sy = x, y
        elif S[y][x] == "G":
            gx, gy = x, y

import queue

q = queue.Queue()
q.put((sx, sy, 0))

seen = [[False] * W for _ in range(H)]
seen[sy][sx] = True

while not q.empty():
    x, y, dist = q.get()

    if x == gx and y == gy:
        print(dist)
        exit()

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if S[ty][tx] not in ".G":
            continue
        if seen[ty][tx]:
            continue
        seen[ty][tx] = True
        q.put((tx, ty, dist + 1))

print(-1)
