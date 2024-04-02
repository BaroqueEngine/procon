def get_error_num(a, b):
    ret = 0
    for i in range(4):
        if a[i] != b[i]:
            ret += 1
    return ret


N = int(input())
A = []
for _ in range(N):
    S, T = input().split()
    T = int(T)
    if T == 1:
        print(S)
        exit()
    A.append((S, T))

candidate = []
for i in range(10000):
    x = str(i).zfill(4)
    ok = True
    for s, t in A:
        if t == 2 and get_error_num(x, s) != 1:
            ok = False
        if t == 3 and get_error_num(x, s) <= 1:
            ok = False
    if ok:
        candidate.append(x)

if len(candidate) == 1:
    print(candidate[0])
else:
    print("Can't Solve")
