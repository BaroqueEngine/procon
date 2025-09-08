H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            continue
        cnt = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if S[ty][tx] == "#":
                cnt += 1
        if cnt not in [2, 4]:
            print("No")
            exit()

print("Yes")