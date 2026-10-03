H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

L = W
R = -1
U = H
D = -1

for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            L = min(L, x)
            R = max(R, x)
            U = min(U, y)
            D = max(D, y)

for y in range(U, D + 1):
    line = []
    for x in range(L, R + 1):
        line.append(S[y][x])
    print("".join(line))