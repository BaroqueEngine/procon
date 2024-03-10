from math import sqrt

T = int(input())

for _ in range(T):
    X = int(input())

    for i in range(2, 10**10):
        if X % i == 0:
            X //= i

            if X % i == 0:
                print(i, X // i)
                break

            print(round(sqrt(X)), i)
            break
