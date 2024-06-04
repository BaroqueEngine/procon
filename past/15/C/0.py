Y, X, R, N = map(int, input().split())


def f(x, y):
    dx = x - X
    dy = y - Y
    return dx * dx + dy * dy <= R**2


for y in range(-N, N + 1):
    line = []
    for x in range(-N, N + 1):
        line.append("#" if f(x, y) else ".")
    print(" ".join(line))
