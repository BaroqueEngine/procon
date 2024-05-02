N, M = map(int, input().split())
G = []
for _ in range(N):
    A = list(map(int, input().split()))
    G.append(A[1:])
P, Q = map(int, input().split())
B = list(map(int, input().split()))

ans = 0
for g in G:
    cnt = 0
    for x in g:
        if x in B:
            cnt += 1
    if cnt >= Q:
        ans += 1
print(ans)