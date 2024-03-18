N = int(input())
A = list(map(int, input().split()))
D = int(input())
ML = []
for i in range(N):
    if i == 0:
        ML.append(A[i])
    else:
        ML.append(max(ML[-1], A[i]))
MR = []
for i in range(N - 1, -1, -1):
    if i == N - 1:
        MR.append(A[i])
    else:
        MR.append(max(MR[-1], A[i]))

for _ in range(D):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    print(max(ML[L - 1], MR[N - R - 2]))
