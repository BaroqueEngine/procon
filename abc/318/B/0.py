N = int(input())
S = [[False] * 101 for _ in range(101)]

for _ in range(N):
    A, B, C, D = map(int, input().split())

    for y in range(A, B):
        for x in range(C, D):
            S[y][x] = True

ans = 0
for row in S:
    ans += sum(row)
print(ans)
