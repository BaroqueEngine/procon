H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
id = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fill(sx, sy, id):
    S[sy][sx] = id
    stack = [(sx, sy)]
    while len(stack) > 0:
        x, y = stack.pop()
        for i in range(len(dx)):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if S[ty][tx] == ".":
                S[ty][tx] = id
                stack.append((tx, ty))

ng_numbers = set()
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            fill(x, y, id)
            id += 1
        if x == 0 or x == W - 1 or y == 0 or y == H - 1:
            if S[y][x] not in ["#", "."]:
                ng_numbers.add(S[y][x])

print(id - len(ng_numbers))