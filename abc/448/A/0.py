N, X = map(int, input().split())
A = list(map(int, input().split()))

for x in A:
    if x < X:
        X = x
        print(1)
    else:
        print(0)