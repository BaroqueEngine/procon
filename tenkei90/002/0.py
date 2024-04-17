import sys
sys.setrecursionlimit(10**7)

def check(s):
    depth = 0
    for c in s:
        if c == "(":
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return False
    return depth == 0

N = int(input())

ans = []

def f(i, s):
    if i == N:
        if check(s):
            ans.append(s)
        return
    f(i + 1, s + "(")            
    f(i + 1, s + ")")

f(0, "")
for s in sorted(ans):
    print(s)