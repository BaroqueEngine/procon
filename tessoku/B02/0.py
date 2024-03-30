A, B = map(int, input().split())
print("Yes" if any([100 % x == 0 for x in range(A, B + 1)]) else "No")
