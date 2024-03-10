W, H = map(int, input().split())
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
X = list(map(int, input().split()))
B = int(input())
Y = list(map(int, input().split()))
piece = (A + 1) * (B + 1)

from bisect import bisect_left
from collections import defaultdict

dic = defaultdict(int)

for x, y in P:
  pos_x = bisect_left(X, x) - 1
  pos_y = bisect_left(Y, y) - 1
  dic[(pos_x, pos_y)] += 1

max_v = 0
min_v = 1000000000000
for v in dic.values():
  max_v = max(max_v, v)
  min_v = min(min_v, v)

if len(dic) < piece:
  min_v = 0

print(min_v, max_v)

  