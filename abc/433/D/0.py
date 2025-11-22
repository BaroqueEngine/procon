from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))

digits = []
for i in range(11):
    digits.append(defaultdict(int))

for x in A:
    digits[len(str(x))][x % M] += 1

ans = 0
for x in A:
	for k in range(1, 11):
          left = x * (10 ** k)
          amari = left % M
          target = (M - amari) % M
          ans += digits[k][target]

print(ans)   