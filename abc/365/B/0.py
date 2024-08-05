N = int(input())
A = list(map(int, input().split()))
B = A[::]
B.sort(reverse=True)

target = B[1]
print(A.index(target) + 1)
