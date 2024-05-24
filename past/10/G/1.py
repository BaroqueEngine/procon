a, b, c = map(int, input().split())


def f(x):
    return x - (a * (x**5) + b * x + c) / (5 * a * (x**4) + b)


x = 2
for _ in range(10):
    x = f(x)
print(x)
