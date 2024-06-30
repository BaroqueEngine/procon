N = int(input())


def factor(x):
    ret = []
    i = 2
    while i * i <= x:
        while x % i == 0:
            ret.append(i)
            x //= i
        i += 1
    if x > 1:
        ret.append(x)
    return ret


f = factor(N)
i = 0
while 2**i < len(f):
    i += 1
print(i)
