A, B, C, D = map(int, input().split())
X = A * 60 + B
Y = C * 60 + D

print("Yes" if Y < X else "No")