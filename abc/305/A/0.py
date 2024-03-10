N = int(input())
if N % 5 == 0:
    print(N)
    exit()

if (N % 5) <= 2:
    print(N // 5 * 5)
else:
    print((N // 5 + 1) * 5)
