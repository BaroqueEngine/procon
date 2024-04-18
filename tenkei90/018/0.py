import math
T = int(input())
L, Z, X = map(int, input().split())

def f(time):
    ratio = -time / T
    rad = math.pi * 2 * ratio - (math.pi / 2)
    cx, cy = 0, L / 2
    x = cx + math.cos(rad) * L / 2
    y = cy + math.sin(rad) * L / 2
    dx = x - X
    dy = 0
    dz = 0 - Z
    width = (dx * dx + dy * dy + dz * dz) ** 0.5 
    height = y
    return math.atan(height / width) * 180 / math.pi

ans = []
Q = int(input())
for _ in range(Q):
    E = int(input())
    ans.append(f(E))
for x in ans:
    print(x)

# pi rad = 180
# 1 rad = 180 / pi
# x rad = 180 / pi * xrad