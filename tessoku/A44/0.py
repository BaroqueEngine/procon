N, Q = map(int, input().split())
A = []
for i in range(N + 1):
    A.append(i)

is_reverse = False
ans = []
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        if is_reverse:
            A[N + 1 - T[1]] = T[2]
        else:
            A[T[1]] = T[2]
    elif T[0] == 2:
        is_reverse = not is_reverse
    else:
        if is_reverse:
            ans.append(A[N + 1 - T[1]])
        else:
            ans.append(A[T[1]])

for x in ans:
    print(x)