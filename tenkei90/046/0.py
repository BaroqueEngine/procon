N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

X = [0] * 46
Y = [0] * 46
Z = [0] * 46

for a in A:
    X[a % 46] += 1
for b in B:
    Y[b % 46] += 1
for c in C:
    Z[c % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += X[i] * Y[j] * Z[k]
print(ans)
