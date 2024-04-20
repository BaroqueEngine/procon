N, Q = map(int, input().split())
T = map(int, input().split())
A = [1] * (N + 1)
A[0] = 0
for x in T:
    A[x] = 1 - A[x]
print(sum(A))
