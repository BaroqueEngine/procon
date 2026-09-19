N = int(input())
C = [[0] * (i + 1) + list(map(int, input().split())) for i in range(N - 1)]

for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if C[a][c] > C[a][b] + C[b][c]:
                print("Yes")
                exit()

print("No")