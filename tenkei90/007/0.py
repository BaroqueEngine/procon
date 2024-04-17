import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

Q = int(input())
for _ in range(Q):
    B = int(input())
    pos = bisect.bisect_left(A, B)
    score = 10**18
    for diff in range(-1, 2):
        if 0 <= pos + diff < N:
            score = min(score, abs(B - A[pos + diff]))
    print(score)