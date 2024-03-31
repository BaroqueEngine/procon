N, K = map(int, input().split())
A = list(map(int, input().split()))

L = A[:N//2]
R = A[N//2:]

set_l = set()
set_r = set()

for bit in range(1, 2 ** len(L)):
    total = 0
    for i in range(len(L)):
        if bit >> i & 1 == 1:
            total += L[i]
    set_l.add(total)
    if total == K:
        print("Yes")
        exit()

for bit in range(1, 2 ** len(R)):
    total = 0
    for i in range(len(R)):
        if bit >> i & 1 == 1:
            total += R[i]
    set_r.add(total)
    if total == K:
        print("Yes")
        exit()

for l in set_l:
    if K - l in set_r:
        print("Yes")
        exit()
print("No")
