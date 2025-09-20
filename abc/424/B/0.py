N, M, K = map(int, input().split())
scores = [0] * N
ans = []
for _ in range(K):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    scores[A] += (2 ** B)
    if scores[A] == (2 ** M) - 1:
        ans.append(A + 1)

print(*ans)