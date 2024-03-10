N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)

ans = []
import bisect

for x in A:
    ans.append(bisect.bisect_left(C, x) + 1)
print(*ans)

ans = []
for x in B:
    ans.append(bisect.bisect_left(C, x) + 1)
print(*ans)
