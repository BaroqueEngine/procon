S = input() + "!"
ans = []

cnt = 0
prev = S[0]
for cur in S:
    if prev == cur:
        cnt += 1
    else:
        ans += [prev, str(cnt)]
        prev = cur
        cnt = 1
print(" ".join(ans))
