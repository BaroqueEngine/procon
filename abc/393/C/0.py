N, M = map(int, input().split())
hist = set([])
ans = 0
for _ in range(M):
    U, V = map(int, input().split())
    if U > V:
        U, V = V, U
    if U == V:
        ans += 1
    elif (U, V) in hist:
        ans += 1
    else:
        hist.add((U, V))
print(ans)