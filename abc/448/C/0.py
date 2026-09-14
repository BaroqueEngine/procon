N, Q = map(int, input().split())
A = list(map(int, input().split()))
P = []
for i in range(N):
    P.append((A[i], i + 1))
P.sort()

ans = []
for _ in range(Q):
    K = int(input())
    B = set(map(int, input().split()))
    found = False
    for i in range(K):
        if P[i][1] not in B:
            ans.append(P[i][0])
            found = True
            break
    if not found:
        ans.append(P[K][0])

for x in ans:
    print(x)