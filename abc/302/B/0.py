H, W = map(int, input().split())
M = [input() for _ in range(H)]
text = "snuke"

def search(x, y, dx, dy):
    i = 0
    max = len(text)

    ok = True
    while i < max:
        if x < 0 or x >= W or y < 0 or y >= H:
            ok = False
            break 

        if M[y][x] != text[i]:
            ok = False
            break
        x += dx
        y += dy

        i += 1

    return ok

for y in range(H):
    for x in range(W):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                result = search(x, y, dx, dy)
                if result:
                     for i in range(len(text)):
                         print(y + 1 + dy * i, x + 1 + dx * i)
                     exit()
