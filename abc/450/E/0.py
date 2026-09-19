
import string

MAX = 105

X = input()
Y = input()
cnt = {chr(ord('a') + i): [0] * MAX for i in range(26)}
for c in X:
    cnt[c][1] += 1

for c in Y:
    cnt[c][2] += 1

size = [0] * MAX
size[1] = len(X)
size[2] = len(Y)

for i in range(3, MAX):
    size[i] = size[i - 1] + size[i - 2]
    for c in string.ascii_lowercase:
        cnt[c][i] = cnt[c][i - 1] + cnt[c][i - 2]

def f(pos, level, c):
    if level == 1:
        return X[:pos].count(c)
    if level == 2:
        return Y[:pos].count(c)

    if pos <= size[level - 1]:
        return f(pos, level - 1, c)
    else:
        return cnt[c][level - 1] + f(pos - size[level - 1], level - 2, c)

ans = []
Q = int(input())
for _ in range(Q):
    L, R, C = input().split()
    L = int(L)
    R = int(R)
    ans.append(f(R, MAX - 1, C) - f(L - 1, MAX - 1 , C))

for x in ans:
    print(x)