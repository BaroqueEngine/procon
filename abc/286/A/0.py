N, A, B, C, D = map(int, input().split())
X = list(map(int, input().split()))

A -= 1
B -= 1
C -= 1
D -= 1

for i in range(B - A + 1):
    X[A + i], X[C + i] = X[C + i], X[A + i]

print(*X)
