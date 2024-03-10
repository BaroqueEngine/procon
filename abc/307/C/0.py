h0, w0 = map(int, input().split())
A = [input() for _ in range(h0)]

h1, w1 = map(int, input().split())
B = [input() for _ in range(h1)]

h2, w2 = map(int, input().split())
X = [input() for _ in range(h2)]


def normalize(S, w, h):
    nw, nh = 0, 0

    left = w - 1
    right = 0
    top = h - 1
    bottom = 0

    for y in range(h):
        for x in range(w):
            if S[y][x] == "#":
                left = min(left, x)
                right = max(right, x)
                top = min(top, y)
                bottom = max(bottom, y)

    nw = right - left + 1
    nh = bottom - top + 1

    ret = []
    for y in range(top, bottom + 1):
        ret.append(S[y][left : right + 1])

    return (ret, nw, nh)


A, w0, h0 = normalize(A, w0, h0)
B, w1, h1 = normalize(B, w1, h1)
X, w2, h2 = normalize(X, w2, h2)


def match(x0, y0, x1, y1):
    C = [["."] * w2 for _ in range(h2)]
    for y in range(h0):
        for x in range(w0):
            C[y + y0][x + x0] = A[y][x]
    for y in range(h1):
        for x in range(w1):
            if B[y][x] == "#":
                C[y + y1][x + x1] = B[y][x]

    for i in range(h2):
        C[i] = "".join(C[i])

    return C == X


for y in range(h2 - h0 + 1):
    for x in range(w2 - w0 + 1):
        for ty in range(h2 - h1 + 1):
            for tx in range(w2 - w1 + 1):
                if match(x, y, tx, ty):
                    print("Yes")
                    exit()

print("No")
