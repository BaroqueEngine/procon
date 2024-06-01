N, L, R = map(int, input().split())
A = []

for i in range(1, L):
    A.append(i)

for i in range(R, L - 1, -1):
    A.append(i)

for i in range(R + 1, N + 1):
    A.append(i)

print(*A)
