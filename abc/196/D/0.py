import sys
sys.setrecursionlimit(10**7)

H, W, A, B = map(int, input().split())


def can_fill(data, tw, th):
    for y in range(H):
        for x in range(W):
            if data[y][x] == 0:
                for ty in range(y, y + th):
                    for tx in range(x, x + tw):
                        if ty >= H:
                            return False
                        if tx >= W:
                            return False
                        if data[ty][tx] != 0:
                            return False
                return True


def fill(data, tw, th, color):
    ret = []
    for line in data:
        ret.append(line[:])

    for y in range(H):
        for x in range(W):
            if data[y][x] == 0:
                for ty in range(y, y + th):
                    for tx in range(x, x + tw):
                        ret[ty][tx] = color
                return ret


def f(data, a, b):
    if a == 0 and b == 0:
        return 1

    ret = 0

    if a > 0:
        if can_fill(data, 2, 1):
            new_data = fill(data, 2, 1, 1)
            ret += f(new_data, a - 1, b)
        if can_fill(data, 1, 2):
            new_data = fill(data, 1, 2, 2)
            ret += f(new_data, a - 1, b)
    if b > 0:
        if can_fill(data, 1, 1):
            new_data = fill(data, 1, 1, 3)
            ret += f(new_data, a, b - 1)
    return ret


data = [[0] * W for _ in range(H)]
print(f(data, A, B))
