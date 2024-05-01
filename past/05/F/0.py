N, M = map(int, input().split())
T = []
for _ in range(M):
    A = list(map(int, input().split()))
    x = 0
    for a in A:
        a -= 1
        x |= (2 ** a)
    T.append(x)

arr = []
for bit in range(2**N):
    x = 0
    for i in range(N):
        if bit >> i & 1 == 1:
            x |= (2 ** i)
    ok = True
    for t in T:
        if x & t == t:
            ok = False
    if ok:
        arr.append(x)

max_cnt = 0
for x in arr:
    cnt = 0
    for i in range(N):
        ok = False
        v = x | (2 ** i)
        for t in T:
            if v & t == t:
                ok = True
        cnt += ok
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
