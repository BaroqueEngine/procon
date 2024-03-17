D = int(input())
N = int(input())

T = [0] * (D + 1)

for _ in range(N):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    T[L] += 1
    T[R + 1] -= 1

cur = 0
for x in T[:D]:
    cur += x
    print(cur)
