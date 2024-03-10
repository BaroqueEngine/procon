H, W = map(int, input().split())
M = [input() for _ in range(H)]

left, right, top, bottom = 10000000000, 0, 1000000000000, 0

for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            left = min(left, x)
            right = max(right, x)
            top = min(top, y)
            bottom = max(bottom, y)

for y in range(top, bottom + 1):
    for x in range(left, right + 1):
        if M[y][x] == ".":
            print(y + 1, x + 1)
            exit()
