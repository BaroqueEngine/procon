H, W = map(int, input().split())
M = [input() for _ in range(H)]
N = int(input())
S = input()

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def f(x, y, S, seen):
    if len(S) == 0:
        print("Yes")
        exit()
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if (tx, ty) in seen:
            continue
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if M[ty][tx] == S[0]:
            seen.add((tx, ty))
            f(tx, ty, S[1:], seen)


for y in range(H):
    for x in range(W):
        if M[y][x] == S[0]:
            f(x, y, S[1:], set([(x, y)]))
print("No")
