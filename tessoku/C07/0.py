import bisect

N = int(input())
C = sorted(list(map(int, input().split())))

S = [0]
for x in C:
    S.append(S[-1] + x)

Q = int(input())
ans = []
for _ in range(Q):
    X = int(input())
    ans.append(bisect.bisect_right(S, X))

for x in ans:
    print(x - 1)