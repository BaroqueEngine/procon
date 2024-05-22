T, N = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(T)]

max_v = [0] * N

for line in P:
    for i in range(N):
        max_v[i] = max(max_v[i], line[i])
    print(sum(max_v))