N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = []
for i in range(N):
    P.append((A[i], B[i], i + 1))

P.sort(key=lambda x: (-(x[0] + x[1]), -x[0], i))

ans = []
for _, _, id in P:
    ans.append(id)

print(*ans)