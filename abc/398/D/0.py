N, Y, X = map(int, input().split())
S = input()
KY, KX = 0, 0
kemuri = set([])
kemuri.add((0, 0))

dir = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0)
}

ans = []
for c in S:
    X -= dir[c][0]
    Y -= dir[c][1]
    KX -= dir[c][0]
    KY -= dir[c][1]

    if (KX, KY) not in kemuri:
        kemuri.add((KX, KY))
    if (X, Y) in kemuri:
        ans.append("1")
    else:
        ans.append("0")

print("".join(ans))