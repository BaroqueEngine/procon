from collections import defaultdict

dic = defaultdict(int)
kind = 0

ans = []
Q = int(input())
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        dic[T[1]] += 1
        if dic[T[1]] == 1:
            kind += 1
    elif T[0] == 2:
        dic[T[1]] -= 1
        if dic[T[1]] == 0:
            kind -= 1
    else:
        ans.append(kind)

for x in ans:
    print(x)
