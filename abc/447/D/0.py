S = input()
a = ab = ans = 0

for c in S:
    if c == "A":
        a += 1
    elif c == "B":
        if a:
            a -= 1
            ab += 1
    else:
        if ab:
            ab -= 1
            ans += 1
print(ans)