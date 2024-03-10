H, W = map(int, input().split())
M = [input() for _ in range(H)]

import sys

sys.setrecursionlimit(10**7)

next_char = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search(x, y, char, seen):
    seen[y * W + x] = True
    if x == W - 1 and y == H - 1:
        print("Yes")
        exit()

    next = next_char[char]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue

        if seen[ty * W + tx]:
            continue

        if M[ty][tx] != next:
            continue

        search(tx, ty, next, seen)


search(0, 0, "s", [False] * (H * W))
print("No")
