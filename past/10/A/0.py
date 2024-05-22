A = list(map(int, input().split()))
INF = 10**18
min_v = INF
max_v = -INF

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        min_v = min(min_v, A[i] * A[j])
        max_v = max(max_v, A[i] * A[j])

print("{} {}".format(min_v, max_v))