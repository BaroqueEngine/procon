N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for bit in range(2**N):
    g = []
    for i in range(N):
        if bit >> i & 1 == 1:
            g.append(i)
    if len(g) == K:
        for i in g:
            ans += A[i]
print(ans)
