H, W, N = map(int, input().split())
T = input()
M = [input() for _ in range(H)]


def f(x, y):
    for dir in T:
        if dir == "L":
            x -= 1
        elif dir == "R":
            x += 1
        elif dir == "U":
            y -= 1
        else:
            y += 1

        if M[y][x] == "#":
            return False
    return True


ans = 0
for y in range(H):
    for x in range(W):
        if M[y][x] == ".":
            ans += f(x, y)
print(ans)
