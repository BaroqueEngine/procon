from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            q.append((x, y))

while len(q) > 0:
    next_white_pos = set([])
    while len(q) > 0:
        x, y = q.popleft()
        if seen[y][x]:
            continue
        seen[y][x] = True

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if S[ty][tx] == "#":
                continue
            next_white_pos.add((tx, ty))

    new_black_pos = set([])
    for x, y in next_white_pos:
        black_num = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if S[ty][tx] == "#":
                black_num += 1
                continue
        if black_num == 1:
            new_black_pos.add((x, y))
    
    for x, y in new_black_pos:
        S[y][x] = "#"
        q.append((x, y))

ans = 0
for y in range(H):
    for x in range(W):
        ans += S[y][x] == "#"
print(ans)
