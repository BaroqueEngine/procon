A, B, C = map(int, input().split())
X = list(map(int, input().split()))
price = [0, B, C]

for i in range(12):
    price[0] += max(0, X[i] - 3) * A
    price[1] += max(0, X[i] - 50) * A

print(min(price))
