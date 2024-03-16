S = list(input())
s = set()

dic = {}
for c in S:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

ans = 0

for a in dic:
    for b in dic:
        if ord(a) >= ord(b):
            continue
        ans += dic[a] * dic[b]

for key in dic:
    if dic[key] >= 2:
        ans += 1
        break

print(ans)
