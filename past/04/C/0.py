H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [-1, 1, 0, 0, -1, 1, -1, 1, 0]
dy = [0, 0, -1, 1, -1, -1, 1, 1, 0]

for y in range(H):
    line = ""
    for x in range(W):
        cnt = 0
        for i in range(len(dx)):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if S[ty][tx] == "#":
                cnt += 1
        line += str(cnt)
    print(line)