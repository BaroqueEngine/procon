N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
ans = []
for _ in range(Q):
    T, D = map(int, input().split())
    T -= 1

    mod = D % A[T][0]
    diff = A[T][1] - mod
    if diff < 0:
        diff += A[T][0]
    D += diff
    ans.append(D)

for x in ans:
    print(x)
