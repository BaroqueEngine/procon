N, K = map(int, input().split())
A = [list(map(int, input().split()))[1:] for _ in range(N)]
C = list(map(int, input().split()))

for i in range(N):
    cnt = len(A[i]) * C[i]
    if cnt < K:
        K -= cnt
    else:
        print(A[i][(K - 1) % len(A[i])])
        break