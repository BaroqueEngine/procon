A = [list(map(int, input().split())) for _ in range(3)]
B = [
    (A[0][0] - A[1][0], A[0][1] - A[1][1]),
    (A[1][0] - A[2][0], A[1][1] - A[2][1]),
    (A[2][0] - A[0][0], A[2][1] - A[0][1]),
]


def f(a, b):
    return a[0] * b[0] + a[1] * b[1] == 0


for i in range(3):
    for j in range(i + 1):
        if f(B[i], B[j]):
            print("Yes")
            exit()
print("No")
