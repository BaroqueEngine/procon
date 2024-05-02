N, L, T, X = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

time = 0
load = 0
retry = 0

while len(G) > 0:
    A, B = G[0]
    if B < L:
        load = 0
        time += A
    elif load + A <= T:
        load += A
        time += A
        if load == T:
            time += X
            load = 0
    else:
        time += T - load
        time += X
        load = 0
        retry += 1
        if retry == 2:
            print("forever")
            exit()
        continue
    G = G[1:]
    retry = 0
print(time)