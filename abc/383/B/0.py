H, W, D = map(int, input().split())
S = [input() for _ in range(H)]
pos = []

for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            pos.append((x, y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def f(x0, y0, x1, y1):
    count = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                continue
            if (abs(x - x0) + abs(y - y0) <= D) or (abs(x - x1) + abs(y - y1) <= D):
                count += 1
    return count


ans = 0
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        ans = max(ans, f(*pos[i], *pos[j]))
print(ans)
