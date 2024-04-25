N = int(input())
cur = int(input())
for _ in range(N - 1):
    X = int(input())
    if cur == X:
        print("stay")
    elif cur < X:
        print("up {}".format(X - cur))
    else:
        print("down {}".format(cur - X))
    cur = X
