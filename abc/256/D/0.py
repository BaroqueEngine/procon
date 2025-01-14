N = int(input())
E = []
for _ in range(N):
    L, R = map(int, input().split())
    E.append((L, 1))
    E.append((R, -1))
E.sort(key=lambda x: (x[0], -x[1]))
ans = []
start, end = None, None

depth = 0
for pos, k in E:
    if depth == 0:
        start = pos
    depth += k
    if depth == 0:
        end = pos
        ans.append((start, end))

for start, end in ans:
    print("{} {}".format(start, end))