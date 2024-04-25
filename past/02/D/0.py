import string
import sys
sys.setrecursionlimit(10**7)
S = input()
dic = {}
for c in string.ascii_lowercase:
    dic[c] = 0
for c in S:
    dic[c] += 1

use = []
for c in dic:
    if dic[c] >= 1:
        use.append(c)

pattern = []


def dfs(i, s):
    if i >= 1:
        pattern.append(s)
    if i == min(3, len(S)):
        return
    for c in use + ["."]:
        dfs(i + 1, s + c)


dfs(0, "")


def create_words(s):
    ret = []

    def f(i, ns):
        if i == len(s):
            ret.append(ns)
            return
        if s[i] == ".":
            for c in use:
                f(i + 1, ns + c)
        else:
            f(i + 1, ns + s[i])
    f(0, "")
    return ret


ans = 0

for p in pattern:
    if p.count(".") == 0:
        if p in S:
            ans += 1
    else:
        words = create_words(p)
        ok = False
        for word in words:
            if word in S:
                ok = True
                break
        if ok:
            ans += 1

print(ans)
