from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
A = [x for x in range(1, N + 1)]
ans = 0

for t in permutations(A, N):
    if P < t < Q:
        ans += 1

print(ans)
