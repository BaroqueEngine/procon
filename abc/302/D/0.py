import bisect
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

value = -1

for x in A:
    pos = bisect.bisect_right(B, x + D) - 1
    if pos >= 0 and abs(x - B[pos]) <= D:
        value = max(value, x + B[pos])
print(value)