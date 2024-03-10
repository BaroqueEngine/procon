H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
SIZE = 9
ans = []

A = [
    "###.?????",
    "###.?????",
    "###.?????",
    "....?????",
    "?????????",
    "?????....",
    "?????.###",
    "?????.###",
    "?????.###",
]


for y in range(H - SIZE + 1):
    for x in range(W - SIZE + 1):
        ok = True
        for ty in range(SIZE):
            for tx in range(SIZE):
                if A[ty][tx] == "?":
                    continue
                if A[ty][tx] != S[y + ty][x + tx]:
                    ok = False

        if ok:
            ans.append((x, y))


for x, y in ans:
    print(y + 1, x + 1)
