import math
A, B, H, M = map(int, input().split())
hour_deg = H / 12 * 360 + M / 60 * 30

minutes_rad = M / 60 * 360 * math.pi / 180
hour_rad = hour_deg * math.pi / 180

mx, my = math.cos(minutes_rad) * B, math.sin(minutes_rad) * B
hx, hy = math.cos(hour_rad) * A, math.sin(hour_rad) * A

dx = mx - hx
dy = my - hy

print(math.sqrt(dx * dx + dy * dy))
