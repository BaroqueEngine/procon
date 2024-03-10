H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]


def clone(A):
    ret = []
    for y in range(H):
        ret.append(A[y][:])
    return ret


def same(A, B):
    return A == B


def shift_w(A, count):
    for _ in range(count):
        temp = []
        for y in range(H):
            temp.append(A[y][0])

        for x in range(1, W):
            for y in range(H):
                A[y][x - 1] = A[y][x]

        for y in range(H):
            A[y][-1] = temp[y]


def shift_h(A, count):
    for _ in range(count):
        temp = A[0][:]
        A.pop(0)
        A.append(temp)


def trace(A):
    for line in A:
        print(line)
    print("---")


for Y in range(H):
    for X in range(W):
        T = clone(A)
        shift_h(T, Y)
        shift_w(T, X)

        if same(T, B):
            print("Yes")
            exit()
print("No")
