N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
B = [sum(v) for v in zip(*X)]

for i in range(M):
    if A[i] > B[i]:
        print("No")
        exit()
print("Yes")
