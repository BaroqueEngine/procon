A = list(map(int, input().split()))
M = sum(A) - max(A) - min(A)
index = A.index(M)
print("ABC"[index])