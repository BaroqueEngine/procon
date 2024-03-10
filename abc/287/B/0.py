N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

cnt = 0
for s in S:
    if s[3:] in T:
        cnt += 1
print(cnt)
