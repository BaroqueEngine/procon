N, K = map(int, input().split())
A = list(map(int, input().split()))

total = (1 + K) * K // 2

A = set(A)
total_a = 0
for x in A:
    if x <= K:
        total_a += x
print(total - total_a)
