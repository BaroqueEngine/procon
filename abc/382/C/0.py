N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for i in range(M):
    C.append((B[i], i))
C.sort()

ans = [-1] * M
for i in range(N):
    while len(C) > 0 and A[i] <= C[-1][0]:
        ans[C[-1][1]] = i + 1
        C.pop()

for x in ans:
    print(x)
