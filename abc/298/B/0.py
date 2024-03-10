N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def eq():
    ok = True
    for y in range(N):
        for x in range(N):
            if A[y][x] == 1 and B[y][x] == 0:
                ok = False
                break
    return ok


def rotate():
    ret = []
    for i in range(N):
        ret.append(A[i][:])

    for y in range(N):
        for x in range(N):
            ret[y][x] = A[N - 1 - x][y]

    return ret


for i in range(4):
    if eq():
        print("Yes")
        exit()
    A = rotate()

print("No")
