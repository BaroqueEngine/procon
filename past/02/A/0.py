S, T = input().split()


def convert(s):
    if s[1] == "F":
        return int(s[0])
    else:
        return -(int(s[1]) - 1)


print(abs(convert(T) - convert(S)))
