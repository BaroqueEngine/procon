N = int(input())
A = list(map(int, input().split()))

print("Yes" if A == [A[0]] * N else "No")
