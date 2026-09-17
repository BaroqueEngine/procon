H, W, Q = map(int, input().split())
ans = []
for _ in range(Q):
    kind, num = map(int, input().split())
    if kind == 1:
        ans.append(num * W)
        H -= num
    else:
        ans.append(num * H)
        W -= num

for x in ans:
    print(x)