N, K = map(int, input().split())

def digit_sum(x):
    return sum(map(int, str(x)))

cnt = 0
for i in range(1, N + 1):
    if digit_sum(i) == K:
        cnt += 1

print(cnt)