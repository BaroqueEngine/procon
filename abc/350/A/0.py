x = int(input()[3:])


def f(x):
    if x == 316:
        return False
    return 1 <= x <= 349


print("Yes" if f(x) else "No")
