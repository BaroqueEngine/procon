N, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

left = -(10**18)
right = 10**18

def dist(x, y):
    total = 0
    for ax, ay in A:
        dx = x - ax
        dy = y - ay
        total += dx * dx + dy * dy
    return total

for _ in range(200):
    mid1 = left + (right - left) / 3
    mid2 = left + (right - left) / 3 * 2
    if dist(mid1, C) > dist(mid2, C):
        left = mid1
    else:
        right = mid2
print(dist(left, C))
