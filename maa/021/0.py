def fact(a, b=1):
    if a == b:
        return 1
    return a * fact(a - 1, b)


n, r = map(int, input().split())
print(fact(n, n - r) // fact(r))
