N, K = map(int, input().split())
C = list(map(int, input().split()))
P = list(map(int, input().split()))

A = []
for i in range(N):
    A.append((P[i], C[i]))
A.sort()

price = 0
seen_color = set()

for p, c in A:
    if c not in seen_color:
        seen_color.add(c)
        price += p
        if len(seen_color) == K:
            print(price)
            exit()
print(-1)