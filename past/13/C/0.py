N = int(input())
A = list(map(int, input().split()))

seen = set()
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            seen.add(A[i] * A[j] * A[k])
print(len(seen))
