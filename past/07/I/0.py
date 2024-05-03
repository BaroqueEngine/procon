import math
N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
c1 = (x1 + x2) / 2
c2 = (y1 + y2) / 2

x1 -= c1
y1 -= c2
x2 -= c1
y2 -= c2

for i in range(N):
    A[i][0] -= c1
    A[i][1] -= c2

base_rad = math.atan2(y2, x2)

for x, y in A:
    length = (x * x + y * y) ** 0.5
    rad = math.atan2(y, x)
    rad -= base_rad
    x = math.cos(rad) * length
    y = math.sin(rad) * length
    print(x, y)
