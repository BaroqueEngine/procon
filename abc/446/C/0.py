from collections import deque

def solve():
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    q = deque([])
    for i in range(N):
        for _ in range(A[i]):
            q.append(i)
        for _ in range(B[i]):
            q.popleft()
        while len(q) > 0:
            if q[0] <= i - D:
                q.popleft()
            else:
                break
    return len(q)


T = int(input())
ans = []
for _ in range(T):
    ans.append(solve())

for x in ans:
    print(x)