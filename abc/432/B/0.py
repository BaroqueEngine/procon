import itertools

X = input()
ans = int(X)
X = list(X)

for l in itertools.permutations(X):
    if l[0] == '0':
        continue
    num = int("".join(l))
    ans = min(ans, num)

print(ans)