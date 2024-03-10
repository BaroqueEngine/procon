from collections import deque

N, M = map(int, input().split())
q = deque(list(map(int, input().split())))

for i in range(1, N + 1):
    if i == q[0]:
        print(0)
        q.popleft()
    elif i < q[0]:
        print(q[0] - i)
