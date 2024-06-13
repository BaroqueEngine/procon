S = input()

prev = S[0]
cnt = 1
ans = ""

for c in S[1:]:
    if c == prev:
        cnt += 1
    else:
        ans += "{}{}".format(prev, cnt)
        cnt = 1
    prev = c
ans += "{}{}".format(prev, cnt)
print(ans)
