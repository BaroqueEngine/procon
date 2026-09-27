T = int(input())
ans = []
for _ in range(T):
    x0, y0, r0, x1, y1, r1 = map(int, input().split())
    dx = x0 - x1
    dy = y0 - y1
    dist_p = dx * dx + dy * dy
    tr_left = abs(r0 - r1)
    tr_right = r0 + r1
    ans.append("Yes" if tr_left ** 2 <= dist_p <= tr_right ** 2 else "No")

for x in ans:
    print(x)