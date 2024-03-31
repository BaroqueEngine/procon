N, S = map(int, input().split())
A = list(map(int, input().split()))
idp = [False] * (S + 1)
idp[0] = True
dp = [idp]

for x in A:
    idp = dp[-1][:]
    for i in range(S + 1):
        if dp[-1][i] and i + x <= S:
            idp[i + x] = True
    dp.append(idp)

if not dp[-1][-1]:
    print(-1)
    exit()

route = []
cur = S
while len(dp) > 1:
    idp = dp.pop()
    x = A.pop()
    if cur - x >= 0 and idp[cur - x]:
        route.append(len(A) + 1)
        cur -= x

print(len(route))
print(*route[::-1])
