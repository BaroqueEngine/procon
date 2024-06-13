N, K = map(int, input().split())


def convert8to10(x):
    ret = 0
    k = 1
    while x > 0:
        ret += (x % 10) * k
        x //= 10
        k *= 8
    return ret


def convert10to9(x):
    if x == 0:
        return 0
    ret = []
    while x > 0:
        ret.append(str(x % 9))
        x //= 9
    ret = ret[::-1]
    return "".join(ret)


def convert8to5(x):
    return int(str(x).replace("8", "5"))


for _ in range(K):
    N = convert8to5(convert10to9(convert8to10(N)))
print(N)
