N = int(input())
A = [0] + list(map(int, input().split()))
pos = [None] * (N + 1)

for i in range(1, N + 1):
    pos[A[i]] = i

ans = []
for i in range(1, N + 1):
    if A[i] != i:
        pos_a, pos_b = i, pos[i]
        val_a, val_b = A[i], i
        ans.append((pos_a, pos_b))
        A[pos_a], A[pos_b] = val_b, val_a
        pos[val_a] = pos_b
        pos[val_b] = pos_a

print(len(ans))
for x, y in ans:
    print(x, y)
