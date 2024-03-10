N = int(input())

def f(x, i):
    d = 10 ** i
    return x // d * d

for i in range(7):
    if N <= 10**(3 + i) - 1:
        print(f(N, i))
        break