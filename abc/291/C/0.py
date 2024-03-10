N = int(input())
S = input()
seen = set()
pos = (0, 0)
seen.add(pos)

for c in S:
    if c == "R":
        pos = (pos[0] + 1, pos[1])
    elif c == "L":
        pos = (pos[0] - 1, pos[1])
    elif c == "U":
        pos = (pos[0], pos[1] + 1)
    else:
        pos = (pos[0], pos[1] - 1)

    if pos in seen:
        print("Yes")
        exit()
    seen.add(pos)
print("No")
