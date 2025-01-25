H, W = map(int, input().split())
M = [input() for _ in range(H)]
left = 10**18
right = -(10**18)
top = 10**18
bottom = -(10**18)

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
            print("No")
            exit()
print("Yes")