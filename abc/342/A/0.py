S = input()
chars = set(S)

for c in chars:
    if S.count(c) == 1:
        print(S.index(c) + 1)
