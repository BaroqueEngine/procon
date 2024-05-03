S = input()
L, R = map(int, input().split())
if len(S) != 1 and S[0] == "0":
    print("No")
    exit()
S = int(S)
print("Yes" if L <= S <= R else "No")
