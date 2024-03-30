import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
ans = []
for _ in range(Q):
    X = int(input())
    ans.append(bisect.bisect_left(A, X))

for x in ans:
    print(x)
