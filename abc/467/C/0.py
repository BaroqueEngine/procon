N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A[0] = 0でスタート
C = A[::]
cnt_0 = 1 if C[0] == 1 else 0
C[0] = 0 

# A[0] = 1でスタート
D = A[::]
cnt_1 = 1 if D[0] == 0 else 0
D[0] = 1

for i in range(N - 1):
    if (C[i] + C[i + 1]) % M != B[i]:
        C[i + 1] += 1
        cnt_0 += 1

    if (D[i] + D[i + 1]) % M != B[i]:
        D[i + 1] += 1
        cnt_1 += 1

print(min(cnt_0, cnt_1))