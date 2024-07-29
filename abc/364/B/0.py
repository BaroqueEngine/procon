H, W = map(int, input().split())
y, x = map(int, input().split())
M = [input() for _ in range(H)]


def onboard(x, y):
    return 1 <= x <= W and 1 <= y <= H and M[y - 1][x - 1] == "."


for c in input():
    if c == "U" and onboard(x, y - 1):
        y -= 1
    elif c == "D" and onboard(x, y + 1):
        y += 1
    elif c == "L" and onboard(x - 1, y):
        x -= 1
    elif c == "R" and onboard(x + 1, y):
        x += 1

print(y, x)
