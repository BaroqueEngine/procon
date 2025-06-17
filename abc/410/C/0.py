N, Q = map(int, input().split())
A = [x for x in range(1, N + 1)]
head = 0
ans = []

for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        P, X = T[1:]
        P -= 1
        A[(head + P) % N] = X
    elif T[0] == 2:
        P = T[1]
        P -= 1
        ans.append(A[(head + P) % N])
    else:
        K = T[1]
        head += K
        head %= N

for x in ans:
    print(x)