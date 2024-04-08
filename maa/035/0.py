x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dx = x1 - x2
dy = y1 - y2

if dx * dx + dy * dy > (r1 + r2) ** 2:
    print(5)
    exit()
if dx * dx + dy * dy == (r1 + r2) ** 2:
    print(4)
    exit()

if r2 > r1:
    x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

if dx * dx + dy * dy == (r1 - r2) ** 2:
    print(2)
    exit()

if dx * dx + dy * dy < (r1 - r2) ** 2:
    print(1)
    exit()

print(3)
