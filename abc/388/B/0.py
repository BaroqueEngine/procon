N, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for k in range(1, D + 1):
    print(max([t * (l + k) for t, l in A]))
