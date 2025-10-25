from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)
for x in A:
    dic[x] += 1

def nc2(x):
    return x * (x - 1) // 2

ans = 0
for key in dic:
    ans += nc2(dic[key]) * (N - dic[key])

print(ans)