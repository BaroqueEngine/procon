S = input()
words = []
word = ""
search = False
for c in S:
    word += c
    if c.isupper():
        if not search:
            search = True
        else:
            search = False
            words.append(word)
            word = ""
words.sort(key=lambda x: x.lower())
ans = ""
for word in words:
    ans += word
print(ans)
