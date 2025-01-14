from collections import deque
q = deque([])
N = int(input())
A = list(map(int, input().split()))
ans = 0

for x in A:
    for i in range(len(q)):
        q[i] += x
    q.append(x)
    while len(q) > 0 and q[0] >= 4:
        q.popleft()
        ans += 1
print(ans)