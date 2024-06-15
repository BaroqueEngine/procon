N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = []
for s in S:
    x = 0
    for i in range(M):
        if s[-(i + 1)] == "o":
            x += 2**i
    T.append(x)

ans = 10**18
for bit in range(1, 2**N):
    v = 0
    cnt = 0
    for i in range(N):
        if bit >> i & 1 == 1:
            cnt += 1
            v |= T[i]
    if v == (2**M) - 1:
        ans = min(ans, cnt)
print(ans)
