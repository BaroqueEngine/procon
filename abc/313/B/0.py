N, M = map(int, input().split())
G = [[] for _ in range(N)]

saikyo = [True] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    saikyo[B] = False

if sum(saikyo) == 1:
    print(saikyo.index(True) + 1)
else:
    print(-1)
