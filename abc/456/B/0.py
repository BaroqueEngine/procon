from itertools import permutations
A = [list(map(int, input().split())) for _ in range(3)]

prob = [[0] * 7 for _ in range(3)]
for y in range(len(A)):
    for x in range(len(A[0])):
        prob[y][A[y][x]] += 1

ans = 0

for i, j, k in permutations([4, 5, 6]):
    ans += prob[0][i] / 6.0 * prob[1][j] / 6.0 * prob[2][k] / 6.0

print(ans)