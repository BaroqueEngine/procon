S = list(map(int, input().split()))
names = "ABCDE"
N = 5
G = []

for bit in range(1, 2**N):
    score = 0
    name = ""
    for i in range(N):
        if bit >> i & 1:
            score += S[i]
            name += names[i]
    G.append((score, name))

G.sort(key=lambda x: (-x[0], x[1]))

for _, name in G:
    print(name)
