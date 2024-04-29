S = input()
T = input()

if S == T:
    print("same")
elif S.upper() == T.upper():
    print("case-insensitive")
else:
    print("different")
