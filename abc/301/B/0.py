N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N - 1):
    if A[i] < A[i + 1]:
        for x in range(A[i], A[i + 1]):
            ans.append(x)
    else:
        for x in range(A[i], A[i + 1], -1):
            ans.append(x)
ans.append(A[-1])
print(*ans)