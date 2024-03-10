H, W = map(int, input().split())
M = [list(input()) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if M[y][x] == ".":
            continue
        if M[y][x] == "#":
            continue

        num = int(M[y][x])

        for ty in range(y - num, y + num + 1):
            for tx in range(x - num, x + num + 1):
                if abs(ty - y) + abs(tx - x) > num:
                    continue
                if tx < 0 or tx >= W or ty < 0 or ty >= H:
                    continue
                if M[ty][tx] == "#":
                    M[ty][tx] = "."

for y in range(H):
    for x in range(W):
        if M[y][x] == ".":
            continue
        if M[y][x] == "#":
            continue
        M[y][x] = "."

for line in M:
    print("".join(line))
