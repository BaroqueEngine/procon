N, M = map(int, input().split())
cur = [0] * (M + 1)
next = [0] * (M + 1)
for _ in range(N):
    A, B = map(int, input().split())
    cur[A] += 1
    next[B] += 1

for x, y in zip(cur[1:], next[1:]):
    print(y - x)