import sys
sys.setrecursionlimit(10**7)
H, W = map(int, input().split())
par = [-1] * (H * W)

def index(x, y):
    return y * W + x

def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def same(a, b):
    return root(a) == root(b)

def unite(a, b):
    a = root(a)
    b = root(b)
    if a == b:
        return
    par[a] += par[b]
    par[b] = a

M = [[False] * W for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Q = int(input())
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        y, x = query[1:]
        y -= 1
        x -= 1
        M[y][x] = True
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if M[ty][tx]:
                unite(index(x, y), index(tx, ty))
    else:
        y1, x1, y2, x2 = query[1:]
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
        if not M[y1][x1] or not M[y2][x2]:
            ans.append("No")
        else:
            ans.append("Yes" if same(index(x1, y1), index(x2, y2)) else "No")

for x in ans:
    print(x)