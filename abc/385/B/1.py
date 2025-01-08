H, W, Y, X = map(int, input().split())
X -= 1
Y -= 1
M = [input() for _ in range(H)]
move = input()
seen = set([])
dir = {}
dir["L"] = (-1, 0)
dir["R"] = (1, 0)
dir["U"] = (0, -1)
dir["D"] = (0, 1)
ans = 0

for c in move:
    X += dir[c][0]
    Y += dir[c][1]
    if M[Y][X] == "#":
        X -= dir[c][0]
        Y -= dir[c][1]
        continue
    if M[Y][X] == "@" and (X, Y) not in seen:
        seen.add((X, Y))
        ans += 1

print("{} {} {}".format(Y + 1, X + 1, ans))
