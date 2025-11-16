N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

S = [x * Y for x in A]
min_weight = min(S)

ans = 0
for i in range(N):
    x = S[i]
    diff = x - min_weight
    if diff % (Y - X) != 0:
        print(-1)
        exit()
    small_num = diff // (Y - X)
    if small_num > A[i]:
        print(-1)
        exit()
    ans += A[i] - small_num

print(ans)    