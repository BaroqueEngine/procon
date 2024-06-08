import sys
sys.setrecursionlimit(10**7)


def f(level, arr, sx, sy):
    if level == 0:
        arr[sy][sx] = "#"
        return
    for y in range(3):
        for x in range(3):
            if x == 1 and y == 1:
                continue
            f(level - 1, arr, sx + x * (3**(level-1)), sy + y * (3**(level-1)))


N = int(input())
arr = [["."] * (3**N) for _ in range(3**N)]
f(N, arr, 0, 0)
for line in arr:
    print("".join(line))
