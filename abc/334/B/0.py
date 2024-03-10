A, M, L, R = map(int, input().split())

A -= L
R -= L
L = 0

A %= M
if A < 0:
    A += M

if A > R:
    print(0)
    exit()
print((R - A) // M + 1)
