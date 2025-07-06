from collections import deque
q = deque([])

ans = []
Q = int(input())
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        C, X = T[1:]
        q.append((X, C))
    else:
        total = 0
        K = T[1]
        while K > 0:
            if K >= q[0][1]:
                K -= q[0][1]
                total += q[0][1] * q[0][0]
                q.popleft()
            else:
                x, c = q.popleft()
                c -= K
                total += x * K
                K = 0
                q.appendleft((x, c))
        ans.append(total)

for x in ans:
    print(x)