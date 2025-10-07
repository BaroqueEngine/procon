S = input()
A = sorted(list(S))
if A[0] == A[1]:
    print(A[-1])
else:
    print(A[0])
