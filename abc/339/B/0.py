H, W, N = map(int, input().split())
M = [list("." * W) for _ in range(H)]

x, y = 0, 0
dir = 0
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for _ in range(N):
    if M[y][x] == '.':
        M[y][x] = '#'
        dir = (dir + 1) % 4
    else:
        M[y][x] = '.'
        dir -= 1
        if dir < 0:
            dir += 4
    x += dirs[dir][0]
    y += dirs[dir][1]
    x %= W
    y %= H
    if x < 0:
        x += W
    if y < 0:
        y += H

for line in M:
    print("".join(line))
