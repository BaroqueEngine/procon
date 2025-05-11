import string

S = input()
for c in string.ascii_letters:
    if c not in S:
        print(c)
        exit()