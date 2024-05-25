N, T = map(int, input().split())
A = list(map(int, input().split()))

X = [0] * N
Y = [0] * N
R = 0
L = 0

for i in range(len(A)):
    index = A[i] - 1
    x = index % N
    y = index // N
    Y[y] += 1
    X[x] += 1
    if x == y:
        R += 1
    if x + y == N - 1:
        L += 1

    if Y[y] == N or X[x] == N or R == N or L == N:
        print(i + 1)
        exit()
print(-1)
