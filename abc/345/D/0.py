import sys
import itertools
sys.setrecursionlimit(10**7)

N, H, W = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]


def is_all_filled(data):
    for y in range(H):
        for x in range(W):
            if data[y][x] == 0:
                return False
    return True


def can_fill(data, tile, sx, sy):
    if sx + tile[0] > W:
        return False
    if sy + tile[1] > H:
        return False

    for y in range(sy, sy + tile[1]):
        for x in range(sx, sx + tile[0]):
            if data[y][x] != 0:
                return False

    return True


def fill(data, tile, sx, sy, num):
    for y in range(sy, sy + tile[1]):
        for x in range(sx, sx + tile[0]):
            data[y][x] = num


def try_fill(data, tile, num):
    for y in range(H):
        for x in range(W):
            if data[y][x] == 0:
                if can_fill(data, tile, x, y):
                    new_data = []
                    for line in data:
                        new_data.append(line[:])
                    fill(new_data, tile, x, y, num)
                    return (True, new_data)
                return (False, data)


def f(data, tiles, index):
    if index == len(tiles):
        if is_all_filled(data):
            print("Yes")
            exit()
        return

    use_tile = tiles[index]
    result, next_data = try_fill(data, use_tile, index + 1)
    if result:
        f(next_data, tiles, index + 1)

    use_tile = [tiles[index][1], tiles[index][0]]
    result, next_data = try_fill(data, use_tile, index + 1)
    if result:
        f(next_data, tiles, index + 1)


for bit in range(1, 2 ** N):
    tiles = []
    tile_num = W * H
    for i in range(N):
        if (bit >> i) & 1 == 1:
            tiles.append(T[i])
            tile_num -= T[i][0] * T[i][1]
    if tile_num != 0:
        continue

    for p in itertools.permutations(tiles):
        p = list(p)
        data = [[0] * W for _ in range(H)]
        f(data, p, 0)
print("No")
