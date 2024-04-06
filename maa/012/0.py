def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x + 1):
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


N = int(input())
print("Yes" if is_prime(N) else "No")
