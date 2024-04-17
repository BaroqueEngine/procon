N = int(input())
S = input()
mod = 10**9+7

dic = {}
for c in "atcoder":
    dic[c] = 0
dic["@"] = 0

prev = {}
for i in range(len("atcoder") - 1):
    prev["atcoder"[i + 1]] = "atcoder"[i]

for c in S:
    if c == "a":
        dic["a"] += 1
    if c in "tcoder":
        dic[c] += dic[prev[c]]
        dic[c] %= mod

print(dic["r"])
