from collections import deque
N, Q = map(int, input().split())
d = list(reversed(["{} {}".format(x, 0) for x in range(1, N + 1)]))
dir = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}

x = 1
y = 0
ans = []

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x += dir[query[1]][0]
        y += dir[query[1]][1]
        d.append("{} {}".format(x, y))
    else:
        ans.append(d[-int(query[1])])

for s in ans:
    print(s)
