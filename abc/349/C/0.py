S = input()
T = list(input().lower())[::-1]

for c in S:
    if c == T[-1]:
        T.pop()
        if len(T) == 1 and T[0] == "x":
            print("Yes")
            exit()
        if len(T) == 0:
            print("Yes")
            exit()
print("No")
