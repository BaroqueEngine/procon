T = int(input())
S = [0] * (T + 1)
N = int(input())
for _ in range(N):
    L, R = map(int, input().split())
    S[L] += 1
    S[R] -= 1

cur = 0
for i in range(T):
    cur += S[i]
    print(cur)
