N, M = map(int, input().split())
cnt = [0] * M
G = [[] for _ in range(N)]
for i in range(M):
    A = list(map(int, input().split()))
    cnt[i] = A[0]
    for x in A[1:]:
        x -= 1
        G[x].append(i)

total = 0
ans = []
B = list(map(int, input().split()))
for x in B:
    x -= 1
    for i in G[x]:
        cnt[i] -= 1
        if cnt[i] == 0:
            total += 1
    ans.append(total)

for x in ans:
    print(x)