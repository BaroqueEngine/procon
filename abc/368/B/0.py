N = int(input())
A = list(map(int, input().split()))

cnt = 0
while sum([x > 0 for x in A]) > 1:
    A.sort(reverse=True)
    A[0] = max(A[0] - 1, 0)
    A[1] = max(A[1] - 1, 0)
    cnt += 1
    # print("#", A)
print(cnt)
