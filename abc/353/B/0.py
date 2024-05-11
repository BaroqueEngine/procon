N, K = map(int, input().split())
A = list(map(int, input().split()))

num = K
cnt = 0

while len(A) > 0:
    while len(A) > 0 and A[0] <= num:
        num -= A[0]
        A.pop(0)

    cnt += 1
    num = K
print(cnt)
