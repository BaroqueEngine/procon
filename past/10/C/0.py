S = input()
index = 0

while len(S) >= 4:
    S = S[:-3]
    index += 1

print("{}{}".format(S, chr(ord("a") + (index - 1))))