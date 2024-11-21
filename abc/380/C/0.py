import itertools

N, K = map(int, input().split())
S = input()
G = []
count = 0
target = None

for c, g in itertools.groupby(S):
    G.append((c, len(list(g))))
    if c == "1":
        count += 1
        if count == K:
            target = G.pop()

count = 0
for i in range(len(G)):
    if G[i][0] == "1":
        count += 1
        if count == K - 1:
            G.insert(i + 1, target)
            break

for char, num in G:
    print(char * num, end="")
print()
