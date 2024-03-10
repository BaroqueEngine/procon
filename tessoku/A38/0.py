D, N = map(int, input().split())
A = [24] * (D + 1)

for _ in range(N):
    L, R, H = map(int, input().split())
    for i in range(L, R + 1):
        A[i] = min(A[i], H)

print(sum(A[1:]))
