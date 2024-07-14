N = int(input())
L = []
R = []
TL = 0
TR = 0
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    TL += l
    TR += r

if not (TL <= 0 <= TR):
    print("No")
    exit()
print("Yes")

diff = -TL
ans = []
for i in range(N):
    min_v = min(R[i] - L[i], diff)
    diff -= min_v
    ans.append(L[i] + min_v)
print(*ans)
