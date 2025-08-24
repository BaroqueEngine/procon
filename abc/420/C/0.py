N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_total = 0
for i in range(N):
    min_total += min(A[i], B[i])

ans = []
for _ in range(Q):
    C, X, V = input().split()
    X = int(X) - 1
    V = int(V)

    now = min(A[X], B[X])
    if C == "A":
        A[X] = V
    else:
        B[X] = V

    min_total += min(V, A[X], B[X]) - now
    ans.append(min_total)


for x in ans:
    print(x)