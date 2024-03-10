N = int(input())
S = input()
T = input()

S = S.replace("1", "l")
S = S.replace("0", "o")

T = T.replace("1", "l")
T = T.replace("0", "o")

print("Yes" if S == T else "No")