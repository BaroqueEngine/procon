N = int(input())
A = [True] * (N + 1)
A[0] = A[1] = False

for i in range(2, N + 1):
    if not A[i]:
        continue

    for j in range(i * 2, N + 1, i):
        A[j] = False

for i in range(N + 1):
    if A[i]:
        print(i)
