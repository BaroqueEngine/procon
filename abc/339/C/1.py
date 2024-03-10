N = int(input())
A = list(map(int, input().split()))

total = 0
min_v = 0

for x in A:
    total += x
    min_v = min(min_v, total)

print(total - min_v)
