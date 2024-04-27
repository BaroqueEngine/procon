N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

for y in range(N):
    for x in range(N):
        if A[y][x] != B[y][x]:
            print(y + 1, x + 1)
            exit()
