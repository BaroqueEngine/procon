N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = N - K
sakes = A[:K]
sake_total = 0
while len(sakes) > 0:
    sake_total += sakes.pop()
    ans += 1
    if sake_total >= X:
        break

if sake_total < X:
    print(-1)
else:
    print(ans)
