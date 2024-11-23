S = input()
seen = set()


def ng():
    print("No")
    exit()


if len(S) % 2 == 1:
    ng()

for i in range(0, len(S), 2):
    text = S[i:i+2]
    if text[0] != text[1]:
        ng()
    if text in seen:
        ng()
    seen.add(text)

print("Yes")
