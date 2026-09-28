N = int(input())
G = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    A = list(map(int, input().split()))[1:]
    for x in A:
        G[x].append(i)

for g in G[1:]:
    print(len(g), *sorted(g))