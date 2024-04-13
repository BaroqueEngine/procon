import sys
sys.setrecursionlimit(10**7)
A, B = map(int, input().split())
ans = []


def f(l, r):
    if l >= r:
        return

    num = r - l
    k = 0
    while 2**(k+1) <= num:
        k += 1

    for i in range(k, -1, -1):
        j = l // (2**i)
        x = (2**i) * j
        y = (2**i) * (j + 1)
        if l <= x and y <= r:
            ans.append((x, y))
            f(l, x)
            f(y, r)
            break


f(A, B)
print(len(ans))
for a, b in ans:
    print(a, b)
