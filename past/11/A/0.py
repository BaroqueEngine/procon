X, A, B, C = map(int, input().split())
usagi = X / A + C
kame = X / B

if usagi == kame:
    print("Tie")
elif usagi < kame:
    print("Hare")
else:
    print("Tortoise")