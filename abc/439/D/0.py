from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

ans = 0
dic = defaultdict(int)
for x in A:
    if x % 5 == 0:
        t = x // 5
        t3 = t * 3
        t7 = t * 7
        ans += dic[t3] * dic[t7]
    dic[x] += 1

dic = defaultdict(int)
for x in reversed(A):
    if x % 5 == 0:
        t = x // 5
        t3 = t * 3
        t7 = t * 7
        ans += dic[t3] * dic[t7]
    dic[x] += 1

print(ans)