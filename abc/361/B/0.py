A = list(map(int, input().split()))
B = list(map(int, input().split()))


def f(A, B):
    x = (A[0] <= B[0] < A[3]) or (B[0] <= A[0] < B[3])
    y = (A[1] <= B[1] < A[4]) or (B[1] <= A[1] < B[4])
    z = (A[2] <= B[2] < A[5]) or (B[2] <= A[2] < B[5])
    return x and y and z


if f(A, B):
    print("Yes")
else:
    print("No")
