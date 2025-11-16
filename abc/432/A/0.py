A = list(map(int, input().split()))
A.sort(reverse=True)
print(A[0] * 100 + A[1] * 10 + A[2])