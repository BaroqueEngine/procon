H, W = map(int, input().split())
S = []
T = []
for _ in range(H):
    S.append(input().count("#"))
for _ in range(H):
    T.append(input().count("#"))

print("Yes" if S == T else "No")
