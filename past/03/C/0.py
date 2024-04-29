A, R, N = map(int, input().split())

if R == 1:
    print(A)
else:
    x = A
    for i in range(N-1):
        x *= R
        if x > 10**9:
            print("large")
            exit()
    print(x)
