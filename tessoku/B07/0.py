T = int(input())
N = int(input())
cnt = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    cnt[L] += 1
    cnt[R] -= 1

num = 0
for x in cnt[:-1]:
    num += x
    print(num)
