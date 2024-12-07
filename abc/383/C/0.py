from collections import deque

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

q = deque([])
for y in range(H):
    for x in range(W):
        if S[y][x] == "H":
            q.append((x, y, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while len(q):
    x, y, step = q.popleft()
    if step == D:
        continue
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if S[ty][tx] != ".":
            continue
        S[ty][tx] = "@"
        q.append((tx, ty, step + 1))

ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] in "H@":
            ans += 1
print(ans)
