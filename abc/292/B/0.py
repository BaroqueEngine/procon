N, Q = map(int, input().split())
R = [0] * N
ans = []

for _ in range(Q):
    t, x = map(int, input().split())
    x -= 1
    if t == 1:
        R[x] += 1
    elif t == 2:
        R[x] = 2
    else:
        ans.append("Yes" if R[x] == 2 else "No")

for x in ans:
    print(x)
