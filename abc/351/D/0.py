H, W = map(int, input().split())
M = [input() for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
free = [[False] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            continue
        ok = True
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if M[ty][tx] == "#":
                ok = False
                break
        if ok:
            free[y][x] = True

level = [[-1] * W for _ in range(H)]

ans = 1
id = 0
for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            continue
        if not free[y][x]:
            continue
        if level[y][x] != -1:
            continue

        level[y][x] = id
        stack = [(x, y)]
        cnt = 0
        while len(stack) > 0:
            cnt += 1
            x, y = stack.pop()
            if not free[y][x]:
                continue
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx < 0 or tx >= W or ty < 0 or ty >= H:
                    continue
                if M[ty][tx] == "#":
                    continue
                if level[ty][tx] == id:
                    continue
                level[ty][tx] = id
                stack.append((tx, ty))
        ans = max(ans, cnt)
        id += 1
print(ans)
