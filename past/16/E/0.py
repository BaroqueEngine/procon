S = input()
if S == "1":
    print(0)
    exit()
if len(S) >= 2 and S[0] == "1" and S[1] == "0" and len(set(S[1:])) == 1:
    print(len(S) - 1)
    exit()
print(len(S))
