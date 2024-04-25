S = input()
dic = {}
for c in "abc":
    dic[c] = 0

for c in S:
    dic[c] += 1

arr = []
for c in "abc":
    arr.append((dic[c], c))

arr.sort()
print(arr[-1][1])
