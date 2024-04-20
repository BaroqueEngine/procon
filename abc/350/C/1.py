N = int(input())
A = [0] + list(map(int, input().split()))
pos = [None] * (N + 1)

for i in range(1, N + 1):
    pos[A[i]] = i

ans = []
for i in range(1, N + 1):
    if A[i] != i:
        j = pos[i]
        ans.append((i, j))
        A[i], A[j] = A[j], A[i]
        pos[A[i]] = i
        pos[A[j]] = j

print(len(ans))
for x, y in ans:
    print(x, y)
