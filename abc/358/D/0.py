from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
A = deque(A)
B = deque(B)

ans = 0
while len(B) > 0:
    if len(A) == 0:
        print(-1)
        exit()
    if A[0] >= B[0]:
        ans += A[0]
        B.popleft()
    A.popleft()
print(ans)
