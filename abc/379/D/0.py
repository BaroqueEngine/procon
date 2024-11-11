from collections import deque

ans = []
now = 0
q = deque([])

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q.append(now)
    elif query[0] == 2:
        now += query[1]
    else:
        num = 0
        while len(q) > 0 and (now - q[0] >= query[1]):
            q.popleft()
            num += 1
        ans.append(num)

for x in ans:
    print(x)
