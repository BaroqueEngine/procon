N = int(input())

ans = 0
L = -1
R = -1

for _ in range(N):
    pos, hand = input().split()
    pos = int(pos)

    if hand == "L":
        if L != -1:
            ans += abs(L - pos)
        L = pos
    else:
        if R != -1:
            ans += abs(R - pos)
        R = pos

print(ans)
