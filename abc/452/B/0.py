H, W = map(int, input().split())

for y in range(H):
    line = []
    for x in range(W):
        if min(x, y) == 0 or x == W - 1 or y == H - 1:
            line.append("#")
        else:
            line.append(".")
    print("".join(line))
