N = int(input())
A = [list(input()) for _ in range(N)]

dic = {}
for x in range(N - 1):
    dic[(x, 0)] = (x + 1, 0)

for y in range(N - 1):
    dic[(-1, y)] = (-1, y + 1)

for x in range(N - 1, 0, -1):
    dic[(x, -1)] = (x - 1, -1)

for y in range(N - 1, 0, -1):
    dic[(0, y)] = (0, y - 1)

import copy

B = copy.deepcopy(A)

for (x, y) in dic:
    tx, ty = dic[(x, y)]
    B[ty][tx] = A[y][x]

for line in B:
    print("".join(line))
