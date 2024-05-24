X, A, B, C = map(int, input().split())
usagi = X * B + C * A * B # X / A + C
kame = X * A # X / B

if usagi == kame:
    print("Tie")
elif usagi < kame:
    print("Hare")
else:
    print("Tortoise")