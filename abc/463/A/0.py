X, Y = map(int, input().split())

if X % 16 != 0:
    print("No")
    exit()

if Y % 9 != 0:
    print("No")
    exit()

print("Yes" if Y // 9 * 16 == X else "No")