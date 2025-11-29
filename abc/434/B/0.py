N, M = map(int, input().split())

nums = [0] * M
weights = [0] * M
for _ in range(N):
    A, B = map(int, input().split())
    A -= 1
    weights[A] += B
    nums[A] += 1

for i in range(M):
    print(weights[i] / nums[i])