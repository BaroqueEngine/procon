S = input()
upper_cnt = 0
for c in S:
    if c.isupper():
        upper_cnt += 1

if upper_cnt > len(S) // 2:
    print(S.upper())
else:
    print(S.lower())
