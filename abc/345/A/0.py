S = input()

if S[0] == "<" and S[-1] == ">" and set(S[1:-1]) == set("="):
    print("Yes")
else:
    print("No")
