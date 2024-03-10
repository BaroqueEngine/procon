N, M, P = map(int, input().split())

if M > N:
    print(0)
else:
    N -= M
    print(N // P + 1)
