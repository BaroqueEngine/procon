N = int(input())
X = []
for _ in range(N):
    A, B = map(int, input().split())
    X.append((A, 1))
    X.append((B + 1, -1))
Q = int(input())
T = []
for _ in range(Q):
    t = int(input())
    T.append(t)
    X.append((t, 999))
X.sort()

ans = {}
cur = 0
for t, x in X:
    if x == 999:
        ans[t] = cur
    else:
        cur += x

for t in T:
    print(ans[t])