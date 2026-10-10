from collections import defaultdict

dic = defaultdict(int)
max_cnt = 0

N = int(input())
for _ in range(N):
    S = input().lower()
    dic[S] += 1
    max_cnt = max(max_cnt, dic[S])

print(max_cnt)
