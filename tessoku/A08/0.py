H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

S = [[0] * (W + 1)]
for line in X:
    s = [0]
    for x in line:
        s.append(s[-1] + x)
    S.append(s)

for x in range(W + 1):
    for y in range(H):
        S[y + 1][x] += S[y][x]

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    print(S[C + 1][D + 1] - S[C + 1][B] - S[A][D + 1] + S[A][B])
