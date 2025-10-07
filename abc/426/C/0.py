from collections import defaultdict
N, Q = map(int, input().split())
dic = defaultdict(int)
for i in range(1, N + 1):
    dic[i] = 1

ans = []
minimum = 1
for _ in range(Q):
    X, Y = map(int, input().split())
    cnt = 0
    for i in range(minimum, X + 1):
        cnt += dic[i]
    ans.append(cnt)
    dic[Y] += cnt
    minimum = max(minimum, X + 1)

for x in ans:
    print(x)