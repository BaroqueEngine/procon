S, T = input().split()


def f(interval, start):
    ret = ""
    for i in range(start, len(S), interval):
        ret += S[i]
    return ret


for i in range(1, len(S)):
    for j in range(0, i):
        if f(i, j) == T:
            print("Yes")
            exit()
print("No")
