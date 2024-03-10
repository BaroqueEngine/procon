A = list(map(int, input().split()))


def a():
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
    return True


def b():
    for i in range(len(A)):
        if not (100 <= A[i] <= 675):
            return False
    return True


def c():
    for i in range(len(A)):
        if not (A[i] % 25 == 0):
            return False
    return True


print("Yes" if a() and b() and c() else "No")
