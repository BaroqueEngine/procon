N, K = map(int, input().split())
X = []
total = 0
for _ in range(N):
    A, B = map(int, input().split())
    X.append((A, B))
    total += B
X.sort()
X.reverse()

if total <= K:
    print(1)
    exit()

while total > K and len(X) > 0:
    day = X[-1][0]
    while len(X) > 0:
        if X[-1][0] == day:
            total -= X[-1][1]
            X.pop()
        else:
            break
print(day + 1)
