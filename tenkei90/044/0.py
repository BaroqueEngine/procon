from collections import deque
N, Q = map(int, input().split())
A = deque(list(map(int, input().split())))
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        A[T[1] - 1], A[T[2] - 1] = A[T[2] - 1], A[T[1] - 1]
    elif T[0] == 2:
        A.appendleft(A.pop())
    else:
        print(A[T[1] - 1])
