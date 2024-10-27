N = 8
arr = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y):
    for i in range(4):
        tx = x
        ty = y
        while 0 <= tx < N and 0 <= ty < N:
            if arr[ty][tx] == "#":
                return True
            tx += dx[i]
            ty += dy[i]
    return False


ans = 0
for y in range(N):
    for x in range(N):
        if not check(x, y):
            ans += 1

print(ans)
