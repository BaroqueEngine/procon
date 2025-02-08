from collections import defaultdict
N = int(input())
P = []
K = [0] * N
for i in range(N):
    A = list(map(int, input().split()))
    K[i], A = A[0], A[1:]
    dic = defaultdict(int)
    for x in A:
        dic[x] += 1 / K[i]
    P.append(dic)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        A, B = P[i], P[j]
        if K[i] > K[j]:
            A, B = B, A
        prob = 0
        for key in A:
            if key in B:
                prob += A[key] * B[key]
        ans = max(ans, prob)
print(ans)
