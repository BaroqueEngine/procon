S = list(input())

base = 1
ans = 0

while len(S) > 0:
    c = S.pop()
    num = ord(c) - ord("A") + 1
    ans += num * base
    base *= 26
print(ans)
