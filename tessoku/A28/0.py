N = int(input())
x = 0
for _ in range(N):
    T, A = input().split()
    A = int(A)

    if T == "+":
        x += A
    elif T == "-":
        x -= A
    else:
        x *= A

    x %= 10000
    print(x)
