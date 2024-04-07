import math
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())


def calc_dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)


mx, my = None, None
for _ in range(100):
    mx = (bx + cx) / 2
    my = (by + cy) / 2
    if calc_dist(ax, ay, bx, by) < calc_dist(ax, ay, cx, cy):
        cx = mx
        cy = my
    else:
        bx = mx
        by = my

print(calc_dist(ax, ay, mx, my))
