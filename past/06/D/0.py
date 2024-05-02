N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for x in A:
    S.append(S[-1] + x)

for i in range(N - K + 1):
    print(S[i + K] - S[i])