N = int(input())
ans = 0
x, y = 0, 0


def f(x0, y0, x1, y1):
    dx = x0 - x1
    dy = y0 - y1
    return (dx * dx + dy * dy) ** 0.5


for _ in range(N):
    A, B = map(int, input().split())
    ans += f(x, y, A, B)
    x, y = A, B

ans += f(x, y, 0, 0)
print(ans)
