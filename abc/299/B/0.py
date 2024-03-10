N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if T not in C:
    T = C[0]

ans = 0
max_value = 0

for i in range(N):
    if C[i] == T and max_value < R[i]:
        max_value = R[i]
        ans = i + 1

print(ans)
