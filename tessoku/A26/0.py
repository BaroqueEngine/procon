def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, x, 2):
        if i * i > x:
            break
        if x % i == 0:
            return False

    return True


Q = int(input())
for _ in range(Q):
    X = int(input())
    if is_prime(X):
        print("Yes")
    else:
        print("No")
