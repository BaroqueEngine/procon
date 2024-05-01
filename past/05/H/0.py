H, W = map(int, input().split())
gy, gx = map(int, input().split())
gx -= 1
gy -= 1
M = [input() for _ in range(H)]
R = [["."] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            R[y][x] = "#"

dir = {
    0: ".>",
    1: ".<",
    2: ".v",
    3: ".^"
}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
stack = [(gx, gy)]
while len(stack) > 0:
    x, y = stack.pop()
    R[y][x] = "o"
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if R[ty][tx] != ".":
            continue
        if M[ty][tx] not in dir[i]:
            continue
        stack.append((tx, ty))
        
for line in R:
    line = "".join(line).replace(".", "x")
    print(line)