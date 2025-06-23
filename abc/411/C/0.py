N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = [0] * (N + 2) # 0=白, 1=黒
black_num = 0

for pos in A:
    D[pos] = 1 - D[pos]
    if D[pos] == 0:
        if D[pos - 1] == D[pos + 1] == 0:
            black_num -= 1
        elif D[pos - 1] == D[pos + 1] == 1:
            black_num += 1
    else:
        if D[pos - 1] == D[pos + 1] == 0:
            black_num += 1
        elif D[pos - 1] == D[pos + 1] == 1:
            black_num -= 1
    print(black_num)