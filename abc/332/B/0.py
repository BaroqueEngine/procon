K, G, M = map(int, input().split())

a, b = 0, 0

for _ in range(K):
    if a == G:
        a = 0
    elif b == 0:
        b = M
    else:
        water = b
        water = min(G - a, water)
        a += water
        b -= water
print("{} {}".format(a, b))
