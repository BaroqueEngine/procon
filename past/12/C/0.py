P = [[None] + list(map(int, input().split())) for _ in range(3)]
prob = [0] * 19

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            x = i + j + k
            prob[x] += P[0][i] * P[1][j] * P[2][k] / (100**3)

for p in prob[1:]:
    print(p)