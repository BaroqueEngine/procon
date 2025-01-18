from collections import deque

que = deque([])

Q = int(input())
diff = 0
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if len(que) == 0:
            que.append((0, query[1]))
        else:
            que.append((que[-1][0] + que[-1][1], query[1]))
    elif query[0] == 2:
        diff += que[0][1]
        que.popleft()
    else:
        ans.append(que[query[1] - 1][0] - diff)

for x in ans:
    print(x)
