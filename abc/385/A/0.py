A = list(map(int, input().split()))
A.sort()

if len(set(A)) == 1:
    print("Yes")
    exit()

print("Yes" if A[0] + A[1] == A[2] else "No")
