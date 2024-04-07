N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

min_dist = 10**18
for i in range(N):
    for j in range(i + 1, N):
        dx = X[i] - X[j]
        dy = Y[i] - Y[j]
        min_dist = min(min_dist, dx * dx + dy * dy)

print(min_dist ** 0.5)
