
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
L.sort()
R.sort()

ans = N * (N - 1) // 2
j = 0
for i in range(N):
    j = max(i, j)
    while j + 1 < N and R[i] >= L[j + 1]:
        j += 1
    ans -= N - 1 - j
print(ans)
