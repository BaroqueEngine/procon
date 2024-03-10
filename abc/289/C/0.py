N, M = map(int, input().split())
A = []

for _ in range(M):
    C = int(input())
    A.append(list(map(int, input().split())))

ans = 0
for i in range(2**M):
    S = set()
    for j in range(M):
        if (i >> j) & 1 == 1:
            for x in A[j]:
                S.add(x)
    if len(S) == N:
        ans += 1
print(ans)
