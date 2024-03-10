S = input()
ans = ""
for c in S:
    if c not in "aiueo":
        ans += c
print(ans)
