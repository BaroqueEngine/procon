N = int(input())
A = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    cnt = A[i] // E[i][0]
    A[i + 1] += cnt * E[i][1]
print(A[-1])
