import math
A, B, H, M = map(int, input().split())
ratio_m = M / 60
ratio_h = H / 12 + M / 60 / 12
rad_m = ratio_m * math.pi * 2
rad_h = ratio_h * math.pi * 2
mx, my = math.cos(rad_m) * B, math.sin(rad_m) * B
hx, hy = math.cos(rad_h) * A, math.sin(rad_h) * A
dx = mx - hx
dy = my - hy
dist = math.sqrt(dx * dx + dy * dy)
print(dist)
