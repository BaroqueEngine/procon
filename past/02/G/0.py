import collections
import string
d = collections.deque()

ans = []
Q = int(input())
for _ in range(Q):
    A = input().split()
    A[0] = int(A[0])
    if A[0] == 1:
        C, X = A[1], int(A[2])
        d.append((C, X))
    else:
        D = int(A[1])
        dic = {}
        for c in string.ascii_lowercase:
            dic[c] = 0
        while D > 0 and len(d) > 0:
            C, X = d.popleft()
            if D >= X:
                D -= X
                dic[C] += X
            else:
                X -= D
                dic[C] += D
                D = 0
                d.appendleft((C, X))
        v = 0
        for c in string.ascii_lowercase:
            v += dic[c] ** 2
        ans.append(v)

for x in ans:
    print(x)
