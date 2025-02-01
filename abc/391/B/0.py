N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for sy in range(N - M + 1):
    for sx in range(N - M + 1):
        ok = True
        for y in range(M):
            for x in range(M):
                if T[y][x] != S[sy + y][sx + x]:
                    ok = False
        if ok:
            print(sy + 1, sx + 1)
            exit()