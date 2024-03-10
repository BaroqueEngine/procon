N = int(input())


def f(x):
    arr = list(map(int, list(str(x))))
    return arr[0] * arr[1] == arr[2]


for i in range(N, N + 1000):
    if f(i):
        print(i)
        exit()
