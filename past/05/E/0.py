H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
left = 10**18
right = 0
top = 10**18
bottom = 0
for y in range(H):
    for x in range(W):
        if T[y][x] == "#":
            left = min(left, x)
            right = max(right, x)
            top = min(top, y)
            bottom = max(bottom, y)
T2 = []
for y in range(top, bottom + 1):
    line = ""
    for x in range(left, right + 1):
        line += T[y][x]
    T2.append(line)
T = T2[:]

def rotate(block):
    ret = []
    W = len(block[0])
    H = len(block)
    for x in range(W):
        line = ""
        for y in range(H):
            line += block[H - 1 - y][x]
        ret.append(line)
    return ret

def match(S, T):
    W2 = len(T[0])
    H2 = len(T)
    for y in range(H - H2 + 1):
        for x in range(W - W2 + 1):
            ok = True
            for ty in range(H2):
                for tx in range(W2):
                    if T[ty][tx] == ".":
                        continue
                    if S[y + ty][x + tx] == "#":
                        ok = False

            if ok:
                return True
    return False

for i in range(4):
    T = rotate(T)
    if match(S[:], T[:]):
        print("Yes")
        exit()
print("No")